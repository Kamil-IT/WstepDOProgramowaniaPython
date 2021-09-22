package com.aggregator.aggregator;

import com.aggregator.aggregator.model.*;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SensorServicesConfig {

    @Bean
    public SensorsService<BeachWaterQuality> beachWaterQualityService() {return new SensorsService<BeachWaterQuality>();}
    @Bean
    public SensorsService<Humidity> humidityService() {return new SensorsService<Humidity>();}
    @Bean
    public SensorsService<PhoneLocation> phoneLocationService() {return new SensorsService<PhoneLocation>();}
    @Bean
    public SensorsService<Temperature> temperatureService() {return new SensorsService<Temperature>();}
    @Bean
    public SensorsService<AirQuality> airQualityService() {return new SensorsService<AirQuality>();}
}
