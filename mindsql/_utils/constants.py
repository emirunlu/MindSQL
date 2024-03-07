LOG_AND_RETURN_CONSTANT = "Output from LLM: {}\nExtracted SQL: {}"
JSON_FILE_ERROR_CONSTANT = "Error loading JSON file: {}"
LOGS_FILE_PATH = "logs/mindsql-{}.log"
LOGS_FORMATTER = "%(levelname)s — %(asctime)s — %(name)s — Function:%(funcName)s — Line:%(lineno)d — %(message)s"
CONNECTION_ESTABLISH_ERROR_CONSTANT = "Connection is None. Please establish a connection first."
NO_DATA_FOUND_IN_JSON_CONSTANT = "No data found in JSON file at {}"
BULK_FALSE_ERROR = "`path` was provided but `bulk` is set to False."
BULK_DATA_SUCCESS_MESSAGE_CONSTANT = "Bulk data processed successfully"
SQL_NOT_PROVIDED_CONSTANT = "Please also provide a SQL query"
ADD_QUESTION_SQL_MESSAGE_CONSTANT = "Adding question and sql...."
ADD_DOCS_MESSAGE_CONSTANT = "Adding documentation...."
ADD_DDL_MESSAGE_CONSTANT = "Adding DDL...."
SUCCESSFULLY_CONNECTED_TO_DB_CONSTANT = "Successfully connected to {} database"
ERROR_CONNECTING_TO_DB_CONSTANT = "Error connecting to {} database\n{}"
INVALID_DB_CONNECTION_OBJECT = "Invalid {} database connection object."
ERROR_WHILE_RUNNING_QUERY = "Error while running query: {}"
MYSQL_SHOW_DATABASE_QUERY = "SHOW DATABASES;"
MYSQL_DB_TABLES_INFO_SCHEMA_QUERY = "SELECT table_name FROM information_schema.tables WHERE table_schema = '{}';"
MYSQL_SHOW_CREATE_TABLE_QUERY = "SHOW CREATE TABLE {};"
POSTGRESQL_SHOW_DATABASE_QUERY = "SELECT datname as DATABASE_NAME FROM pg_database WHERE datistemplate = false;"
POSTGRESQL_DB_TABLES_INFO_SCHEMA_QUERY = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_catalog = '{db}';"
ERROR_DOWNLOADING_SQLITE_DB_CONSTANT = "Error downloading sqlite db: {}"
SQLLITE_GET_DB_QUERY = "SELECT DISTINCT name FROM pragma_database_list;"
SQLLIE_TABLE_INFO_SCHEMA_CONSTANT = "SELECT name FROM sqlite_master WHERE type='table';"
SQLLITE_TRAINING_DATASET_QUERY_CONSTANT = "SELECT sql FROM sqlite_master WHERE name = '{}';"
GOOGLE_GEN_AI_VALUE_ERROR = "For GoogleGenAI, config must be provided with an api_key"
GOOGLE_GEN_AI_APIKEY_ERROR = "config must contain a Google AI Studio api_key"
LLAMA_VALUE_ERROR = "For LlamaAI, config must be provided with a model_path"
LLAMA_PROMPT_EXCEPTION = "Prompt cannot be empty."
OPENAI_VALUE_ERROR = "OpenAI API key is required"
OPENAI_PROMPT_EMPTY_EXCEPTION = "Prompt cannot be empty."
POSTGRESQL_SHOW_CREATE_TABLE_QUERY = """SELECT 'CREATE TABLE "' || table_name || '" (' || array_to_string(array_agg(column_name || ' ' || data_type), ', ') || ');' AS create_statement FROM information_schema.columns WHERE table_name = '{table}' GROUP BY table_name;"""
