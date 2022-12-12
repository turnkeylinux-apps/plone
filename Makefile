COMMON_CONF += apache-credit

CREDIT_LOCATION = ~ "^/(?!(.*manage|.*manage_main|.*plugins))"

include $(FAB_PATH)/common/mk/turnkey/apache.mk
include $(FAB_PATH)/common/mk/turnkey.mk
