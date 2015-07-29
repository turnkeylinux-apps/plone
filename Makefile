COMMON_CONF = apache-credit apache-vhost
COMMON_OVERLAYS = apache

CREDIT_LOCATION = ~ "^/(?!(.*manage|.*manage_main|.*plugins))"

include $(FAB_PATH)/common/mk/turnkey.mk
