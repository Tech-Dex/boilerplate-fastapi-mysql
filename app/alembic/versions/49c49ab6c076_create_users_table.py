"""create users table

Revision ID: 49c49ab6c076
Revises: None
Create Date: 2022-01-06 12:19:26.089395

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "49c49ab6c076"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("username", sa.String(255), nullable=False),
        sa.Column("hashed_password", sa.String(255), nullable=False),
        sa.Column("salt", sa.String(255), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("is_active", sa.Boolean, nullable=False, default=False),
        sa.Column("first_name", sa.String(255), nullable=False),
        sa.Column("second_name", sa.String(255), nullable=True),
        sa.Column("last_name", sa.String(255), nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
        sa.Column("deleted_at", sa.DateTime, nullable=True),
    )

    op.create_index("users_username_idx", "users", ["username"], unique=True)

    op.create_index("users_email_idx", "users", ["email"], unique=True)


def downgrade():
    op.drop_table("users")
