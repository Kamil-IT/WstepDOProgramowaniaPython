package com.aggregator.aggregator;

import com.aggregator.aggregator.model.*;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@AllArgsConstructor
@RestController
public class PostController {

    private SensorsService<BeachWaterQuality> beachWaterQualitySensorsService;
    private SensorsService<Humidity> humiditySensorsService;
    private SensorsService<PhoneLocation> phoneLocationSensorsService;
    private SensorsService<Temperature> temperatureSensorsService;
    private SensorsService<AirQuality> airQualitySensorsService;


    @PostMapping("/water-quality")
    void postBeachWaterQuality(@RequestBody BeachWaterQuality beachWaterQuality){
        log.info("Http: " + beachWaterQuality.toString());
        beachWaterQualitySensorsService.addEntity(beachWaterQuality);
    }

    @PostMapping("/phone-location")
    void postPhoneLocation(@RequestBody PhoneLocation phoneLocation){
        log.info("Http: " + phoneLocation.toString());
        phoneLocationSensorsService.addEntity(phoneLocation);
    }

    @PostMapping("/temperature")
    void postTemperature(@RequestBody Temperature temperature){
        log.info("Http: " + temperature.toString());
        temperatureSensorsService.addEntity(temperature);
    }

    @PostMapping("/air-quality")
    void postAirQuality(@RequestBody AirQuality airQuality){
        log.info("Http: " + airQuality.toString());
        airQualitySensorsService.addEntity(airQuality);
    }

    @PostMapping("/humidity")
    void postHumidity(@RequestBody Humidity humidity){
        log.info("Http: " + humidity.toString());
        humiditySensorsService.addEntity(humidity);
    }
}
