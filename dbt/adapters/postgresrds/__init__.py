from dbt.adapters.base import AdapterPlugin

from dbt.adapters.postgresrds.column import PostgresColumn
from dbt.adapters.postgresrds.connections import PostgresRDSConnectionManager, PostgresCredentials
from dbt.adapters.postgresrds.impl import PostgresAdapter
from dbt.adapters.postgresrds.relation import PostgresRelation
from dbt.include import postgresrds


Plugin = AdapterPlugin(
    adapter=PostgresAdapter,  # type: ignore
    credentials=PostgresCredentials,
    include_path=postgresrds.PACKAGE_PATH,
)
