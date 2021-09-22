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

    private Service<BeachWaterQuality> beachWaterQualityService;
    private Service<Humidity> humidityService;
    private Service<PhoneLocation> phoneLocationService;
    private Service<Temperature> temperatureService;
    private Service<AirQuality> airQualityService;


    public MqttController(Service<BeachWaterQuality> beachWaterQualityService,
                          Service<Humidity> humidityService,
                          Service<PhoneLocation> phoneLocationService,
                          Service<Temperature> temperatureService,
                          Service<AirQuality> airQualityService) {
        this.beachWaterQualityService = beachWaterQualityService;
        this.humidityService = humidityService;
        this.phoneLocationService = phoneLocationService;
        this.temperatureService = temperatureService;
        this.airQualityService = airQualityService;
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
                    beachWaterQualityService.addEntity(beachWaterQuality);

                        break;
                    case "phone_location":
                        PhoneLocation phoneLocation = objectMapper.readValue(payload, PhoneLocation.class);
                        phoneLocationService.addEntity(phoneLocation);
                        break;
                    case "temperature":
                        Temperature temperature = objectMapper.readValue(payload, Temperature.class);
                        temperatureService.addEntity(temperature);
                        break;
                    case "air-quality":
                        AirQuality airQuality = objectMapper.readValue(payload, AirQuality.class);
                        airQualityService.addEntity(airQuality);
                        break;
                    case "humidity":
                        Humidity humidity = objectMapper.readValue(payload, Humidity.class);
                        humidityService.addEntity(humidity);
                        break;
                    default:
                        log.warn("Topic dont much to standards");
                }

            }

        };
    }
}
