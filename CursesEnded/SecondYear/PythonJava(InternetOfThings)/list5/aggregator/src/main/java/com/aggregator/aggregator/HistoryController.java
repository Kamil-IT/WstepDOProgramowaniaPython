package com.aggregator.aggregator;

import com.aggregator.aggregator.converter.DataConverter;
import com.aggregator.aggregator.model.BeachWaterQuality;
import com.aggregator.aggregator.model.PhoneLocation;
import com.google.gson.Gson;
import lombok.AllArgsConstructor;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;

@AllArgsConstructor
@Controller
public class HistoryController {

    public final SensorsService<BeachWaterQuality> beachWaterQualitySensorsService;
    public final SensorsService<PhoneLocation> phoneLocationSensorsService;

    @GetMapping("/history")
    public String getHistory(Model model) {
        model.addAttribute("sensorTitles", Arrays.asList(
                "Beach water quality",
                "Phone location"
        ));
//        model.addAttribute("sensorTitles", Arrays.asList(
//                "Beach water quality",
//                "Phone location"
//        ));

        return "/historygenerator";
    }


    @RequestMapping(value = "/historydoc", produces = MediaType.APPLICATION_JSON_VALUE, method = RequestMethod.GET)
    public String getHistoryHandler(
            Model model,
            @RequestParam("app") Integer number,
            @RequestParam("datestart") String dateStart,
            @RequestParam("timestart") String timeStart,
            @RequestParam("dateend") String dateEnd,
            @RequestParam("timeend") String timeEnd,
            @RequestParam(value = "graphic", required = false) boolean graphic
    ) {
        Date start = DataConverter.getDataFromString(dateStart, timeStart);
        Date end = DataConverter.getDataFromString(dateEnd, timeEnd);
        String json = null;
        if (!graphic) {
            Gson gson = new Gson();
            if (number == 1) {
                json = gson.toJson(beachWaterQualitySensorsService.getEntitiesBetween(start, end));
            } else {
                json = gson.toJson(phoneLocationSensorsService.getEntitiesBetween(start, end));
            }
            model.addAttribute("val", json);
            return "/empty.html";
        } else {
            List<Double> data;
            String name;
            String title;
            if (number == 1) {
                name = "Temperature";
                title = "Beach Water Quality Sensors";
                data = beachWaterQualitySensorsService.getEntitiesBetween(start, end)
                        .stream()
                        .map(BeachWaterQuality::getTemp)
                        .collect(Collectors.toList());
            } else {
                name = "Latitude";
                title = "Phone Location Sensors";
                data = phoneLocationSensorsService.getEntitiesBetween(start, end)
                        .stream()
                        .map(PhoneLocation::getLatitude)
                        .collect(Collectors.toList());
            }
            List<Integer> labels = new ArrayList<>();
            for (int i = 0; i < data.size(); i++) {
                labels.add(i);
            }
            model.addAttribute("data", data);
            model.addAttribute("name", name);
            model.addAttribute("title", title);
            model.addAttribute("labels", labels);
            return "/historygraphic.html";
        }
    }
}
