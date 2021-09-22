package com.aggregator.aggregator;

import com.aggregator.aggregator.model.*;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.annotation.Bean;
import org.springframework.integration.annotation.ServiceActivator;
import org.springframework.messaging.Message;
import org.springframework.messaging.MessageHandler;
import org.springframework.stereotype.Component;

@Slf4j
@Component
public class MqttController {

    static final String MQTT_PUBLISHER_ID = "spring-server";
    static final String MQTT_SERVER_ADDRESS = "tcp://127.0.0.1:1883";

    private SensorsService<BeachWaterQuality> beachWaterQualitySensorsService;
    private SensorsService<Humidity> humiditySensorsService;
    private SensorsService<PhoneLocation> phoneLocationSensorsService;
    private SensorsService<Temperature> temperatureSensorsService;
    private SensorsService<AirQuality> airQualitySensorsService;


    public MqttController(SensorsService<BeachWaterQuality> beachWaterQualitySensorsService,
                          SensorsService<Humidity> humiditySensorsService,
                          SensorsService<PhoneLocation> phoneLocationSensorsService,
                          SensorsService<Temperature> temperatureSensorsService,
                          SensorsService<AirQuality> airQualitySensorsService) {
        this.beachWaterQualitySensorsService = beachWaterQualitySensorsService;
        this.humiditySensorsService = humiditySensorsService;
        this.phoneLocationSensorsService = phoneLocationSensorsService;
        this.temperatureSensorsService = temperatureSensorsService;
        this.airQualitySensorsService = airQualitySensorsService;
    }


    @Bean
    @ServiceActivator(inputChannel = "mqttInputChannel")
    public MessageHandler handler() {
        return new MessageHandler() {

            @SneakyThrows
            @Override
            public void handleMessage(Message<?> message) {
                String payload = (String) message.getPayload();
                ObjectMapper objectMapper = new ObjectMapper();
                objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
                log.info("Mqtt: " + payload);
                switch ((String) message.getHeaders().get("mqtt_receivedTopic")) {
                    case "beach_water_quality":
                    BeachWaterQuality beachWaterQuality = objectMapper.readValue(payload, BeachWaterQuality.class);
                    beachWaterQualitySensorsService.addEntity(beachWaterQuality);

                        break;
                    case "phone_location":
                        PhoneLocation phoneLocation = objectMapper.readValue(payload, PhoneLocation.class);
                        phoneLocationSensorsService.addEntity(phoneLocation);
                        break;
                    case "temperature":
                        Temperature temperature = objectMapper.readValue(payload, Temperature.class);
                        temperatureSensorsService.addEntity(temperature);
                        break;
                    case "air-quality":
                        AirQuality airQuality = objectMapper.readValue(payload, AirQuality.class);
                        airQualitySensorsService.addEntity(airQuality);
                        break;
                    case "humidity":
                        Humidity humidity = objectMapper.readValue(payload, Humidity.class);
                        humiditySensorsService.addEntity(humidity);
                        break;
                    default:
                        log.warn("Topic dont much to standards");
                }

            }

        };
    }
}
