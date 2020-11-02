package com.aggregator.aggregator;

import com.aggregator.aggregator.model.*;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.stereotype.Controller;

@Configuration
public class ConfigServices {

    @Bean
    public Service<BeachWaterQuality> beachWaterQualityService() {return new Service<BeachWaterQuality>();}
    @Bean
    public Service<Humidity> humidityService() {return new Service<Humidity>();}
    @Bean
    public Service<PhoneLocation> phoneLocationService() {return new Service<PhoneLocation>();}
    @Bean
    public Service<Temperature> temperatureService() {return new Service<Temperature>();}
    @Bean
    public Service<AirQuality> airQualityService() {return new Service<AirQuality>();}
}
