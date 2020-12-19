from enum import Enum
'''

ERROR EXAMPLE:
import sqlErrors

new = sqlErrors.sql_error_data_exception.invalid_argument_for_logarithm
new2 = sqlErrors.sql_error_no_data.no_additional_dynamic_result_sets_returned

print("ERROR "+new.value+": "+str(new.name))
print("ERROR "+new2.value+": "+str(new2.name))

OUTPUT:
ERROR 2201E: invalid_argument_for_logarithm
ERROR 02001: no_additional_dynamic_result_sets_returned

'''
    # Class 00 — Successful Completion    
class sql_error_successful_completion(Enum):
    successful_completion = '00000'
    # Class 01 — Warning
class sql_error_warning(Enum):
    warning = '01000'
    dynamic_result_sets_returned = '0100C'
    implicit_zero_bit_padding = '01008'
    null_value_eliminated_in_set_function = '01003'
    privilege_not_granted = '01007'
    privilege_not_revoked = '01006'
    string_data_right_truncation = '01004'
    deprecated_feature = '01P01'
    # Class 02 — No Data (this is also a warning class per the SQL standard)
class sql_error_no_data(Enum):
    no_data = '02000'	
    no_additional_dynamic_result_sets_returned = '02001'
    # Class 03 — SQL Statement Not Yet Complete
class sql_error_statemet_not_yet_complete(Enum):
    sql_statement_not_yet_complete = '03000'
    # Class 08 — Connection Exception
class sql_error_error_connection(Enum):
    connection_exception = '08000'
    connection_does_not_exist = '08003'
    connection_failure = '08006'
    sqlclient_unable_to_establish_sqlconnection = '08001'
    sqlserver_rejected_establishment_of_sqlconnection = '08004'
    transaction_resolution_unknown = '08007'
    protocol_violation = '08P01'
    # Class 09 — Triggered Action Exception
class sql_error_action_exception(Enum):
    triggered_action_exception = '09000'
    # Class 0A — Feature Not Supported
class sql_error_not_supported(Enum):
    feature_not_supported = '0A000'
    # Class 0B — Invalid Transaction Initiation
class sql_error_invalid_transaction(Enum):
    invalid_transaction_initiation = '0B000'
    # Class 0F — Locator Exception
class sql_error_locator_exception(Enum):
    locator_exception = '0F000'
    invalid_locator_specification = '0F001'
    # Class 0L — Invalid Grantor
class sql_error_invalid_grantor(Enum):
    invalid_grantor = '0L000'
    invalid_grant_operation = '0LP01'
    # Class 0P — Invalid Role Specification
class sql_error_role_specification(Enum):
    invalid_role_specification = '0P000'
    # Class 0Z — Diagnostics Exception
class sql_error_diagnostics_exception(Enum):
    diagnostics_exception = '0Z000'
    stacked_diagnostics_accessed_without_active_handler = '0Z002'
    # Class 20 — Case Not Found
class sql_error_not_found(Enum):
    case_not_found = '20000'
    # Class 21 — Cardinality Violation
class sql_error_cardanlity_violation(Enum):
    cardinality_violation = '21000'
    # Class 22 — Data Exception
class sql_error_data_exception(Enum):
    data_exception = '22000'
    array_subscript_error = '2202E'
    character_not_in_repertoire = '22021'
    datetime_field_overflow = '22008'
    division_by_zero = '22012'
    error_in_assignment = '22005'
    escape_character_conflict = '2200B'
    indicator_overflow = '22022'
    interval_field_overflow = '22015'
    invalid_argument_for_logarithm = '2201E'
    invalid_argument_for_ntile_function = '22014'
    invalid_argument_for_nth_value_function = '22016'
    invalid_argument_for_power_function = '2201F'
    invalid_argument_for_width_bucket_function = '2201G'
    invalid_character_value_for_cast = '22018'
    invalid_datetime_format = '22007'
    invalid_escape_character = '22019'
    invalid_escape_octet = '2200D'
    invalid_escape_sequence = '22025'
    nonstandard_use_of_escape_character = '22P06'
    invalid_indicator_parameter_value = '22010'
    invalid_parameter_value = '22023'
    invalid_preceding_or_following_size = '22013'
    invalid_regular_expression = '2201B'
    invalid_row_count_in_limit_clause = '2201W'
    invalid_row_count_in_result_offset_clause = '2201X'
    invalid_tablesample_argument = '2202H'
    invalid_tablesample_repeat = '2202G'
    invalid_time_zone_displacement_value = '22009'
    invalid_use_of_escape_character = '2200C'
    most_specific_type_mismatch = '2200G'
    null_value_not_allowed = '22004'
    null_value_no_indicator_parameter = '22002'
    numeric_value_out_of_range = '22003'
    sequence_generator_limit_exceeded = '2200H'
    string_data_length_mismatch = '22026'
    string_data_right_truncation = '22001'
    substring_error = '22011'
    trim_error = '22027'
    unterminated_c_string = '22024'
    zero_length_character_string = '2200F'
    floating_point_exception = '22P01'
    invalid_text_representation = '22P02'
    invalid_binary_representation = '22P03'
    bad_copy_file_format = '22P04'
    untranslatable_character = '22P05'
    not_an_xml_document = '2200L'
    invalid_xml_document = '2200M'
    invalid_xml_content = '2200N'
    invalid_xml_comment = '2200S'
    invalid_xml_processing_instruction = '2200T'
    duplicate_json_object_key_value = '22030'
    invalid_argument_for_sql_json_datetime_function = '22031'
    invalid_json_text = '22032'
    invalid_sql_json_subscript = '22033'
    more_than_one_sql_json_item = '22034'
    no_sql_json_item = '22035'
    non_numeric_sql_json_item = '22036'
    non_unique_keys_in_a_json_object = '22037'
    singleton_sql_json_item_required = '22038'
    sql_json_array_not_found = '22039'
    sql_json_member_not_found = '2203A'
    sql_json_number_not_found = '2203B'
    sql_json_object_not_found = '2203C'
    too_many_json_array_elements = '2203D'
    too_many_json_object_members = '2203E'
    sql_json_scalar_required = '2203F'
    # Class 23 — Integrity Constraint Violation
class sql_error_integrity_constraint_violation(Enum):
    integrity_constraint_violation = '23000'
    restrict_violation = '23001'
    not_null_violation = '23502'
    foreign_key_violation = '23503'
    unique_violation = '23505'
    check_violation = '23514'
    exclusion_violation = '23P01'
    # Class 24 — Invalid Cursor State
class sql_error_invalid_cursor_state(Enum):
    invalid_cursor_state = '24000'
    # Class 25 — Invalid Transaction State
class sql_error_invalid_transaction_state(Enum):
    invalid_transaction_state = '25000'
    active_sql_transaction = '25001'
    branch_transaction_already_active = '25002'
    held_cursor_requires_same_isolation_level = '25008'
    inappropriate_access_mode_for_branch_transaction = '25003'
    inappropriate_isolation_level_for_branch_transaction = '25004'
    no_active_sql_transaction_for_branch_transaction = '25005'
    read_only_sql_transaction = '25006'
    schema_and_data_statement_mixing_not_supported = '25007'
    no_active_sql_transaction = '25P01'
    in_failed_sql_transaction = '25P02'
    idle_in_transaction_session_timeout = '25P03'
    # Class 26 — Invalid SQL Statement Name
class sql_error_invalid_sql_statement_name(Enum):
    invalid_sql_statement_name = '26000'
    # Class 27 — Triggered Data Change Violation
class sql_error_data_change_violation(Enum):
    triggered_data_change_violation = '27000'
    # Class 28 — Invalid Authorization Specification
class sql_error_invalid_authorization_specification(Enum):
    invalid_authorization_specification = '28000'
    invalid_password = '28P01'
    # Class 2B — Dependent Privilege Descriptors Still Exist
class sql_error_privilege_descriptors_still_exist(Enum):
    dependent_privilege_descriptors_still_exist = '2B000'
    dependent_objects_still_exist = '2BP01'
    # Class 2D — Invalid Transaction Termination
class sql_error_invalid_transaction_termination(Enum):
    invalid_transaction_termination = '2D000'
    # Class 2F — SQL Routine Exception
class sql_error_routine_exception(Enum):
    sql_routine_exception = '2F000'
    function_executed_no_return_statement = '2F005'
    modifying_sql_data_not_permitted = '2F002'
    prohibited_sql_statement_attempted = '2F003'
    reading_sql_data_not_permitted = '2F004'
    # Class 34 — Invalid Cursor Name
class sql_error_invalid_cursor_name(Enum):
    invalid_cursor_name = '34000'
    # Class 38 — External Routine Exception
class sql_error_external_routine_exception(Enum):
    external_routine_exception = '38000'
    containing_sql_not_permitted = '38001'
    modifying_sql_data_not_permitted = '38002'
    prohibited_sql_statement_attempted = '38003'
    reading_sql_data_not_permitted = '38004'
    # Class 39 — External Routine Invocation Exception
class sql_error_external_routine_invocation_exception(Enum):
    external_routine_invocation_exception = '39000'
    invalid_sqlstate_returned = '39001'
    null_value_not_allowed = '39004'
    trigger_protocol_violated = '39P01'
    srf_protocol_violated = '39P02'
    event_trigger_protocol_violated = '39P03'
    # Class 3B — Savepoint Exception
class sql_error_savepoint_exception(Enum):
    savepoint_exception = '3B000'
    invalid_savepoint_specification = '3B001'
    # Class 3D — Invalid Catalog Name
class sql_error_invalid_catalog_name(Enum):
    invalid_catalog_name = '3D000'
    # Class 3F — Invalid Schema Name
class sql_error_invalid_schema_name(Enum):
    invalid_schema_name = '3F000'
    # Class 40 — Transaction Rollback
class sql_error_transaction_rollback(Enum):
    transaction_rollback = '40000'
    transaction_integrity_constraint_violation = '40002'
    serialization_failure = '40001'
    statement_completion_unknown = '40003'
    deadlock_detected = '40P01'
    # Class 42 — Syntax Error or Access Rule Violation
class sql_error_syntax_error_or_access_rule_violation(Enum):
    syntax_error_or_access_rule_violation = '42000'
    syntax_error = '42601'
    insufficient_privilege = '42501'
    cannot_coerce = '42846'
    grouping_error = '42803'
    windowing_error = '42P20'
    invalid_recursion = '42P19'
    invalid_foreign_key = '42830'
    invalid_name = '42602'
    name_too_long = '42622'
    reserved_name = '42939'
    datatype_mismatch = '42804'
    indeterminate_datatype = '42P18'
    collation_mismatch = '42P21'
    indeterminate_collation = '42P22'
    wrong_object_type = '42809'
    generated_always = '428C9'
    undefined_column = '42703'
    undefined_function = '42883'
    undefined_table = '42P01'
    undefined_parameter = '42P02'
    undefined_object = '42704'
    duplicate_column = '42701'
    duplicate_cursor = '42P03'
    duplicate_database = '42P04'
    duplicate_function = '42723'
    duplicate_prepared_statement = '42P05'
    duplicate_schema = '42P06'
    duplicate_table = '42P07'
    duplicate_alias = '42712'
    duplicate_object = '42710'
    ambiguous_column = '42702'
    ambiguous_function = '42725'
    ambiguous_parameter = '42P08'
    ambiguous_alias = '42P09'
    invalid_column_reference = '42P10'
    invalid_column_definition = '42611'
    invalid_cursor_definition = '42P11'
    invalid_database_definition = '42P12'
    invalid_function_definition = '42P13'
    invalid_prepared_statement_definition = '42P14'
    invalid_schema_definition = '42P15'
    invalid_table_definition = '42P16'
    invalid_object_definition = '42P17'
    # Class 44 — WITH CHECK OPTION Violation
class sql_error_with_check_option_violation(Enum):
    with_check_option_violation = '44000'
    # Class 53 — Insufficient Resources
class sql_error_insufficient_resources(Enum):
    insufficient_resources = '53000'
    disk_full = '53100'
    out_of_memory = '53200'
    too_many_connections = '53300'
    configuration_limit_exceeded = '53400'
    # Class 54 — Program Limit Exceeded
class sql_error_program_limit_exceeded(Enum):
    program_limit_exceeded = '54000'
    statement_too_complex = '54001'
    too_many_columns = '54011'
    too_many_arguments = '54023'
    # Class 55 — Object Not In Prerequisite State
class sql_error_object_not_in_prerequisite_state(Enum):
    object_not_in_prerequisite_state = '55000'
    object_in_use = '55006'
    cant_change_runtime_param = '55P02'
    lock_not_available = '55P03'
    unsafe_new_enum_value_usage = '55P04'
    # Class 57 — Operator Intervention
class sql_error_operator_intervention(Enum):
    operator_intervention = '57000'
    query_canceled = '57014'
    admin_shutdown = '57P01'
    crash_shutdown = '57P02'
    cannot_connect_now = '57P03'
    database_dropped = '57P04'
    # Class 58 — System Error (errors external to PostgreSQL itself)
class sql_error_system_error(Enum):
    system_error = '58000'
    io_error = '58030'
    undefined_file = '58P01'
    duplicate_file = '58P02'
    # Class 72 — Snapshot Failure
class sql_error_snapshot_too_old(Enum):
    snapshot_too_old = '72000'
    # Class F0 — Configuration File Error
class sql_error_config_file_error(Enum):
    config_file_error = 'F0000'
    lock_file_exists = 'F0001'
    # Class HV — Foreign Data Wrapper Error (SQL/MED)
class sql_error_fdw_error(Enum):
    fdw_error = 'HV000'
    fdw_column_name_not_found = 'HV005'
    fdw_dynamic_parameter_value_needed = 'HV002'
    fdw_function_sequence_error = 'HV010'
    fdw_inconsistent_descriptor_information = 'HV021'
    fdw_invalid_attribute_value = 'HV024'
    fdw_invalid_column_name = 'HV007'
    fdw_invalid_column_number = 'HV008'
    fdw_invalid_data_type = 'HV004'
    fdw_invalid_data_type_descriptors = 'HV006'
    fdw_invalid_descriptor_field_identifier = 'HV091'
    fdw_invalid_handle = 'HV00B'
    fdw_invalid_option_index = 'HV00C'
    fdw_invalid_option_name = 'HV00D'
    fdw_invalid_string_length_or_buffer_length = 'HV090'
    fdw_invalid_string_format = 'HV00A'
    fdw_invalid_use_of_null_pointer = 'HV009'
    fdw_too_many_handles = 'HV014'
    fdw_out_of_memory = 'HV001'
    fdw_no_schemas = 'HV00P'
    fdw_option_name_not_found = 'HV00J'
    fdw_reply_handle = 'HV00K'
    fdw_schema_not_found = 'HV00Q'
    fdw_table_not_found = 'HV00R'
    fdw_unable_to_create_execution = 'HV00L'
    fdw_unable_to_create_reply = 'HV00M'
    fdw_unable_to_establish_connection = 'HV00N'
    # Class P0 — PL/pgSQL Error
class sql_error_plpgsql_error(Enum):
    plpgsql_error = 'P0000'
    raise_exception = 'P0001'
    no_data_found = 'P0002'
    too_many_rows = 'P0003'
    assert_failure = 'P0004'
    # Class XX — Internal Error
class sql_error_internal_error(Enum):
    internal_error = 'XX000'
    data_corrupted = 'XX001'
    index_corrupted = 'XX002'