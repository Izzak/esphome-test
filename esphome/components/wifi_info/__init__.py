import esphome.codegen as cg
import esphome.config_validation as cv
import esphome.final_validate as fv
from esphome import automation
from esphome.automation import Condition
from esphome.const import (
    CONF_AP,
    CONF_BSSID,
    CONF_CHANNEL,
    CONF_DNS1,
    CONF_DNS2,
    CONF_DOMAIN,
    CONF_ENABLE_BTM,
    CONF_ENABLE_RRM,
    CONF_FAST_CONNECT,
    CONF_GATEWAY,
    CONF_HIDDEN,
    CONF_ID,
    CONF_MANUAL_IP,
    CONF_NETWORKS,
    CONF_PASSWORD,
    CONF_POWER_SAVE_MODE,
    CONF_REBOOT_TIMEOUT,
    CONF_SSID,
    CONF_STATIC_IP,
    CONF_SUBNET,
    CONF_USE_ADDRESS,
    CONF_PRIORITY,
    CONF_IDENTITY,
    CONF_CERTIFICATE_AUTHORITY,
    CONF_CERTIFICATE,
    CONF_KEY,
    CONF_USERNAME,
    CONF_EAP,
    CONF_ON_CONNECT,
    CONF_ON_DISCONNECT,
)
from esphome.core import CORE, HexInt, coroutine_with_priority
from esphome.components.esp32 import add_idf_sdkconfig_option, get_esp32_variant, const
from esphome.components.network import IPAddress
