from opcua import ua

import logging

################################################################################
# class: Config
################################################################################

class Config:
    logLevel = logging.WARNING

################################################################################
# class: DevelopmentConfig
################################################################################

class DevelopmentConfig (Config):
    # Mongo Config
    mongoUrl      = "mongodb://localhost"
    mongoDatabase = "ClimateFront"

    # OPC UA Server Stock Simulation Config
    serverOPCUASimulationEndpoint       = "opc.tcp://localhost:4840/stock"
    serverOPCUASimulationSecurityIds    = "Anonymous"
    serverOPCUASimulationSecurityPolicy = ua.SecurityPolicyType.NoSecurity