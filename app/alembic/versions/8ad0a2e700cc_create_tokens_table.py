"""create tokens table

Revision ID: 8ad0a2e700cc
Revises: 49c49ab6c076
Create Date: 2022-01-06 12:16:11.012808

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "8ad0a2e700cc"
down_revision = "49c49ab6c076"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "tokens",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("subject", sa.String(length=255), nullable=False),
        sa.Column("expire", sa.DateTime, nullable=False),
        sa.Column("token", sa.String(255), nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
        sa.Column("deleted_at", sa.DateTime, nullable=True),
    )

    op.create_foreign_key(
        "fk_tokens_user_id", "tokens", "users", ["user_id"], ["id"], ondelete="CASCADE"
    )

    op.create_index("ix_tokens_token", "tokens", ["token"], unique=True)


def downgrade():
    op.drop_table("tokens")
