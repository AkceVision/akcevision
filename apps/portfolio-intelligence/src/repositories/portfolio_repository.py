import os
import sqlite3
from uuid import uuid4

from src.models.portfolio import Holding, Portfolio


class PortfolioRepository:
    def __init__(self, db_path: str | None = None):
        self.db_path = db_path or os.getenv(
            "PORTFOLIO_DB_PATH",
            "data/portfolio.db",
        )

        parent = os.path.dirname(self.db_path)

        if parent:
            os.makedirs(parent, exist_ok=True)

        self._initialize_database()

    def _connect(self):
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize_database(self):
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS portfolios (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    base_currency TEXT NOT NULL
                )
                """
            )

            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS holdings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    portfolio_id TEXT NOT NULL,
                    symbol TEXT NOT NULL,
                    quantity REAL NOT NULL,
                    average_price REAL NOT NULL,
                    currency TEXT NOT NULL,
                    FOREIGN KEY (portfolio_id)
                        REFERENCES portfolios(id)
                        ON DELETE CASCADE
                )
                """
            )

            connection.commit()

    def create(
        self,
        name: str,
        base_currency: str,
    ) -> Portfolio:
        portfolio = Portfolio(
            id=str(uuid4()),
            name=name,
            base_currency=base_currency,
            holdings=[],
        )

        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO portfolios (
                    id,
                    name,
                    base_currency
                )
                VALUES (?, ?, ?)
                """,
                (
                    portfolio.id,
                    portfolio.name,
                    portfolio.base_currency,
                ),
            )

            connection.commit()

        return portfolio

    def get(
        self,
        portfolio_id: str,
    ) -> Portfolio | None:
        with self._connect() as connection:
            portfolio_row = connection.execute(
                """
                SELECT
                    id,
                    name,
                    base_currency
                FROM portfolios
                WHERE id = ?
                """,
                (portfolio_id,),
            ).fetchone()

            if portfolio_row is None:
                return None

            holding_rows = connection.execute(
                """
                SELECT
                    symbol,
                    quantity,
                    average_price,
                    currency
                FROM holdings
                WHERE portfolio_id = ?
                ORDER BY id
                """,
                (portfolio_id,),
            ).fetchall()

        holdings = [
            Holding(
                symbol=row["symbol"],
                quantity=row["quantity"],
                average_price=row["average_price"],
                currency=row["currency"],
            )
            for row in holding_rows
        ]

        return Portfolio(
            id=portfolio_row["id"],
            name=portfolio_row["name"],
            base_currency=portfolio_row["base_currency"],
            holdings=holdings,
        )

    def add_holding(
        self,
        portfolio_id: str,
        holding: Holding,
    ) -> Portfolio | None:
        portfolio = self.get(portfolio_id)

        if portfolio is None:
            return None

        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO holdings (
                    portfolio_id,
                    symbol,
                    quantity,
                    average_price,
                    currency
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    portfolio_id,
                    holding.symbol,
                    holding.quantity,
                    holding.average_price,
                    holding.currency,
                ),
            )

            connection.commit()

        return self.get(portfolio_id)
