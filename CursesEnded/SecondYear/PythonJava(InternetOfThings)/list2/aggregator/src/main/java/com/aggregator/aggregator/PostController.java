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

    private Service<BeachWaterQuality> beachWaterQualityService;
    private Service<Humidity> humidityService;
    private Service<PhoneLocation> phoneLocationService;
    private Service<Temperature> temperatureService;
    private Service<AirQuality> airQualityService;


    @PostMapping("/water-quality")
    void postBeachWaterQuality(@RequestBody BeachWaterQuality beachWaterQuality){
        log.info("Http: " + beachWaterQuality.toString());
        beachWaterQualityService.addEntity(beachWaterQuality);
    }

    @PostMapping("/phone-location")
    void postPhoneLocation(@RequestBody PhoneLocation phoneLocation){
        log.info("Http: " + phoneLocation.toString());
        phoneLocationService.addEntity(phoneLocation);
    }

    @PostMapping("/temperature")
    void postTemperature(@RequestBody Temperature temperature){
        log.info("Http: " + temperature.toString());
        temperatureService.addEntity(temperature);
    }

    @PostMapping("/air-quality")
    void postAirQuality(@RequestBody AirQuality airQuality){
        log.info("Http: " + airQuality.toString());
        airQualityService.addEntity(airQuality);
    }

    @PostMapping("/humidity")
    void postHumidity(@RequestBody Humidity humidity){
        log.info("Http: " + humidity.toString());
        humidityService.addEntity(humidity);
    }
}
