package com.aggregator.aggregator;

import com.aggregator.aggregator.model.*;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestAttribute;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

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
        beachWaterQualityService.addEntity(beachWaterQuality);
    }

    @PostMapping("/phone-location")
    void postPhoneLocation(@RequestBody PhoneLocation phoneLocation){
        phoneLocationService.addEntity(phoneLocation);
    }

    @PostMapping("/temperature")
    void postTemperature(@RequestBody Temperature temperature){
        temperatureService.addEntity(temperature);
    }

    @PostMapping("/air-quality")
    void postAirQuality(@RequestBody AirQuality airQuality){
        airQualityService.addEntity(airQuality);
    }

    @PostMapping("/humidity")
    void postHumidity(@RequestBody Humidity humidity){
        humidityService.addEntity(humidity);
    }
}
