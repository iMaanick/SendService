from sqlalchemy import BigInteger, DateTime, ForeignKey, String, Table, Column

from app.infrastructure.db.models.base import metadata

auth_sessions_table = Table(
    "auth_sessions",
    metadata,
    Column("id", String, primary_key=True),
    Column("user_id", BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("expiration", DateTime(timezone=True), nullable=False),
)
