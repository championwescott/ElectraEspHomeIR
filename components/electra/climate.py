import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate_ir
from esphome.const import CONF_ID

AUTO_LOAD = ["climate_ir"]
CODEOWNERS = ["@omersht"]

CONF_SUPPORTS_OFF_COMMAND = 'supports_off_command'
electra_ns = cg.esphome_ns.namespace("electra")
ElectraClimate = electra_ns.class_("ElectraClimate", climate_ir.ClimateIR)

CONFIG_SCHEMA = climate_ir.CLIMATE_IR_WITH_RECEIVER_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(ElectraClimate),
        cv.Optional(CONF_SUPPORTS_OFF_COMMAND, default=True): cv.boolean,

    }
)


async def to_code(config):
    var = await climate_ir.new_climate_ir(config)
    cg.add(var.setOffSupport(config[CONF_SUPPORTS_OFF_COMMAND]))
