COMMON_CONF = apache-credit postfix-local apache-vhost
CREDIT_LOCATION = ~ "^/(?!(.*manage|.*manage_main|.*plugins))"

include $(FAB_PATH)/common/mk/turnkey.mk
