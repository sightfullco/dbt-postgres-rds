from dbt.adapters.postgresrds.relation_configs.constants import (
    MAX_CHARACTERS_IN_IDENTIFIER,
)
from dbt.adapters.postgresrds.relation_configs.index import (
    PostgresIndexConfig,
    PostgresIndexConfigChange,
)
from dbt.adapters.postgresrds.relation_configs.materialized_view import (
    PostgresMaterializedViewConfig,
    PostgresMaterializedViewConfigChangeCollection,
)
