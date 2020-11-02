package com.aggregator.aggregator;

import com.aggregator.aggregator.model.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.Calendar;
import java.util.Date;
import java.util.OptionalDouble;

@Controller
public class IndexController {

    @Value("${sensor.time.show.hour:hour}")
    private Integer sensorTimeToShowHour = 1;

    private Service<BeachWaterQuality> beachWaterQualityService;
    private Service<Humidity> humidityService;
    private Service<PhoneLocation> phoneLocationService;
    private Service<Temperature> temperatureService;
    private Service<AirQuality> airQualityService;

    public IndexController(Service<BeachWaterQuality> beachWaterQualityService,
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

    @GetMapping(value = {"/", "/index"})
    public String getIndex(Model model) {
        System.out.print(sensorTimeToShowHour);

        Calendar calendar = Calendar.getInstance();
        calendar.setTime(new Date());
        calendar.set(Calendar.HOUR_OF_DAY, calendar.get(Calendar.HOUR_OF_DAY) - sensorTimeToShowHour);
        Date time = calendar.getTime();

        int sizeWater = beachWaterQualityService.getEntitiesAfter(time).size();
        OptionalDouble avgWater = beachWaterQualityService.getEntitiesAfter(time).stream().mapToDouble(BeachWaterQuality::getTemp).average();
        model.addAttribute("water_quality_count", String.valueOf(sizeWater));
        model.addAttribute("water_quality_avg", String.valueOf(avgWater.orElse(0)));

        int sizeLocation = phoneLocationService.getEntitiesAfter(time).size();
        OptionalDouble avgLat = phoneLocationService.getEntitiesAfter(time).stream().mapToDouble(PhoneLocation::getLatitude).average();
        OptionalDouble avgLong = phoneLocationService.getEntitiesAfter(time).stream().mapToDouble(PhoneLocation::getLongitude).average();
        model.addAttribute("phone_location_count", String.valueOf(sizeLocation));
        model.addAttribute("phone_location_avg_lat", String.valueOf(avgLat.orElse(0)));
        model.addAttribute("phone_location_avg_long", String.valueOf(avgLong.orElse(0)));

        int sizeTem = temperatureService.getEntitiesAfter(time).size();
        OptionalDouble avgTemInside = temperatureService.getEntitiesAfter(time).stream().filter(e -> e.getOutside_inside().equals("inside")).mapToDouble(Temperature::getTemp).average();
        OptionalDouble avgTemOutside = temperatureService.getEntitiesAfter(time).stream().filter(e -> e.getOutside_inside().equals("outside")).mapToDouble(Temperature::getTemp).average();
        model.addAttribute("temperature_count", sizeTem);
        model.addAttribute("temperature_avg_inside", String.valueOf(avgTemInside.orElse(0)));
        model.addAttribute("temperature_avg_outside", String.valueOf(avgTemOutside.orElse(0)));

        int sizeAir = airQualityService.getEntitiesAfter(time).size();
        OptionalDouble avgAir = airQualityService.getEntitiesAfter(time).stream().mapToDouble(AirQuality::getNitrogenDioxideMicrogramsPerCubicMetre).average();
        model.addAttribute("air_quality_count", String.valueOf(sizeAir));
        model.addAttribute("air_quality_avg", String.valueOf(avgAir.orElse(0)));

        int sizeHum = humidityService.getEntitiesAfter(time).size();
        OptionalDouble avgHum = humidityService.getEntitiesAfter(time).stream().mapToDouble(Humidity::getHumidity).average();
        model.addAttribute("humidity_count", String.valueOf(sizeHum));
        model.addAttribute("humidity_avg", String.valueOf(avgHum.orElse(0)));

        return "/index";
    }
}
