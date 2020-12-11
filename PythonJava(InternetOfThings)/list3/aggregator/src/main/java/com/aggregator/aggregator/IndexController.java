package com.aggregator.aggregator;

import com.aggregator.aggregator.model.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import javax.websocket.server.PathParam;
import java.util.*;

@Controller
public class IndexController {

    @Value("${sensor.time.show.hour:hour}")
    private Integer sensorTimeToShowHour = 1;

    private SensorsService<BeachWaterQuality> beachWaterQualitySensorsService;
    private SensorsService<Humidity> humiditySensorsService;
    private SensorsService<PhoneLocation> phoneLocationSensorsService;
    private SensorsService<Temperature> temperatureSensorsService;
    private SensorsService<AirQuality> airQualitySensorsService;
    private SensorConfigService sensorConfigService;

    public IndexController(SensorsService<BeachWaterQuality> beachWaterQualitySensorsService,
                           SensorsService<Humidity> humiditySensorsService,
                           SensorsService<PhoneLocation> phoneLocationSensorsService,
                           SensorsService<Temperature> temperatureSensorsService,
                           SensorsService<AirQuality> airQualitySensorsService,
                           SensorConfigService sensorConfigService) {
        this.sensorTimeToShowHour = sensorTimeToShowHour;
        this.beachWaterQualitySensorsService = beachWaterQualitySensorsService;
        this.humiditySensorsService = humiditySensorsService;
        this.phoneLocationSensorsService = phoneLocationSensorsService;
        this.temperatureSensorsService = temperatureSensorsService;
        this.airQualitySensorsService = airQualitySensorsService;
        this.sensorConfigService = sensorConfigService;
    }

    @GetMapping(value = {"/", "/index"})
    public String getIndex(Model model) {
        System.out.print(sensorTimeToShowHour);

        Calendar calendar = Calendar.getInstance();
        calendar.setTime(new Date());
        calendar.set(Calendar.HOUR_OF_DAY, calendar.get(Calendar.HOUR_OF_DAY) - sensorTimeToShowHour);
        Date time = calendar.getTime();

        int sizeWater = beachWaterQualitySensorsService.getEntitiesAfter(time).size();
        OptionalDouble avgWater = beachWaterQualitySensorsService.getEntitiesAfter(time).stream().mapToDouble(BeachWaterQuality::getTemp).average();
        Configuration app1Config = sensorConfigService.getApp1Config();
        model.addAttribute("water_quality_count", String.valueOf(sizeWater));
        model.addAttribute("water_quality_avg", String.valueOf(avgWater.orElse(0)));
        model.addAttribute("water_quality_non_status", app1Config.getStatus());
        model.addAttribute("water_quality_protocol", app1Config.getProtocol());

        int sizeLocation = phoneLocationSensorsService.getEntitiesAfter(time).size();
        OptionalDouble avgLat = phoneLocationSensorsService.getEntitiesAfter(time).stream().mapToDouble(PhoneLocation::getLatitude).average();
        OptionalDouble avgLong = phoneLocationSensorsService.getEntitiesAfter(time).stream().mapToDouble(PhoneLocation::getLongitude).average();
        Configuration app2Config = sensorConfigService.getApp2Config();
        model.addAttribute("phone_location_count", String.valueOf(sizeLocation));
        model.addAttribute("phone_location_avg_lat", String.valueOf(avgLat.orElse(0)));
        model.addAttribute("phone_location_avg_long", String.valueOf(avgLong.orElse(0)));


        int sizeTem = temperatureSensorsService.getEntitiesAfter(time).size();
        OptionalDouble avgTemInside = temperatureSensorsService.getEntitiesAfter(time).stream().filter(e -> e.getOutside_inside().equals("inside")).mapToDouble(Temperature::getTemp).average();
        OptionalDouble avgTemOutside = temperatureSensorsService.getEntitiesAfter(time).stream().filter(e -> e.getOutside_inside().equals("outside")).mapToDouble(Temperature::getTemp).average();
        model.addAttribute("temperature_count", sizeTem);
        model.addAttribute("temperature_avg_inside", String.valueOf(avgTemInside.orElse(0)));
        model.addAttribute("temperature_avg_outside", String.valueOf(avgTemOutside.orElse(0)));

        int sizeAir = airQualitySensorsService.getEntitiesAfter(time).size();
        OptionalDouble avgAir = airQualitySensorsService.getEntitiesAfter(time).stream().mapToDouble(AirQuality::getNitrogenDioxideMicrogramsPerCubicMetre).average();
        model.addAttribute("air_quality_count", String.valueOf(sizeAir));
        model.addAttribute("air_quality_avg", String.valueOf(avgAir.orElse(0)));

        int sizeHum = humiditySensorsService.getEntitiesAfter(time).size();
        OptionalDouble avgHum = humiditySensorsService.getEntitiesAfter(time).stream().mapToDouble(Humidity::getHumidity).average();
        model.addAttribute("humidity_count", String.valueOf(sizeHum));
        model.addAttribute("humidity_avg", String.valueOf(avgHum.orElse(0)));

        return "/index";
    }

    @PostMapping("/update")
    public String postConfig(@PathParam("app") Integer app, @PathParam("protocol") String protocol, @PathParam("frequency") String frequency, @PathParam("status") String status){
        Map<String, String> mapParam = new HashMap<>();
        mapParam.put("protocol", protocol);
        mapParam.put("frequency", frequency);
        mapParam.put("status", status);
        switch(app){
            case 1:
                sensorConfigService.postApp1Config(mapParam);
                break;
            case 2:
                sensorConfigService.postApp2Config(mapParam);
                break;
            case 3:
                sensorConfigService.postApp3Config(mapParam);
                break;
            case 4:
                sensorConfigService.postApp4Config(mapParam);
                break;
            case 5:
                sensorConfigService.postApp5Config(mapParam);
                break;
            default:
                System.out.println("I cant send it ;/");
        }
        return "redirect:/index";
    }

    @PostMapping("/updateactuator")
    public String postConfigActuator(@PathParam("actuator") String actuator){
        Map<String, String> mapParam = new HashMap<>();
        if (actuator == null){
            mapParam.put("actuator", "off");
        }
        else {
            mapParam.put("actuator", "on");
        }
        sensorConfigService.postApp3Config(mapParam);
        return "redirect:/index";
    }
}
