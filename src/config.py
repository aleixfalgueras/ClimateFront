import logging

from opcua import ua


################################################################################
# class: Config
################################################################################

class Config:
    DEMO_OPCUA_LOG_LEVEL = logging.ERROR
    API_REST_LOG_LEVEL = logging.INFO

################################################################################
# class: DevelopmentConfig
################################################################################

class DevelopmentConfig (Config):
    # Mongo Config
    MONGO_URL      = "mongodb://localhost"
    MONGO_DATABASE = "ClimateFront"

    # OPC UA Server Stock Simulation Config
    SERVER_OPCUA_SIMULATION_ENDPOINT        = "opc.tcp://localhost:4840/stock"
    SERVER_OPCUA_SIMULATION_SECURITY_IDS    = "Anonymous"
    SERVER_OPCUA_SIMULATION_SECURITY_POLICY = ua.SecurityPolicyType.NoSecurity

    # API REST Config
    API_REST_PORT = 8080

    # Services - OpenWeatherMap
    API_KEY = "fa5363235e9d90bef24be9a929e7f9c7"
    API_BASE_CALL = "https://api.openweathermap.org/data/2.5/forecast?appid=" + API_KEY