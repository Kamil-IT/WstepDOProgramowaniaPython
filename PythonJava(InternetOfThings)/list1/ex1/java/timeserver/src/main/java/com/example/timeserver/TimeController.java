package com.example.timeserver;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import javax.websocket.server.PathParam;
import java.time.ZoneId;
import java.util.Calendar;
import java.util.Date;
import java.util.TimeZone;

import static java.util.Calendar.*;
import static java.util.Calendar.HOUR_OF_DAY;

@RestController
public class TimeController {

    @GetMapping(value = "time")
    public String getCurrentTimeByTimeZone(@PathParam(value = "tz") String tz){
        Calendar calendar = getInstance();
        calendar.setTime(new Date());
        calendar.setTimeZone(TimeZone.getTimeZone("GMT" + tz));
        String sTime = calendar.get(HOUR_OF_DAY) + ":" +
                calendar.get(MINUTE) + ":" + calendar.get(SECOND);
        System.out.println("GET: " + sTime);
        return sTime;
    }
}
