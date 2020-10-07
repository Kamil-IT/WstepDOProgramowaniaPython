package com.example.timeserver;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import javax.websocket.server.PathParam;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Calendar;
import java.util.Date;
import java.util.TimeZone;

import static java.util.Calendar.*;

@RestController
public class TimeController {

    public static final String BASE_FILE_FOR_REQUESTS = "request/request";

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

    @PostMapping(value = "time")
    public String getJsonMessage(@RequestBody String message){
        System.out.println("POST: " + message);

        String fileName = getAvailableFileName();
        Path newFilePath = Paths.get(fileName);

        try {
            Files.createFile(newFilePath);
            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
            writer.write(message);
            writer.close();

            System.out.println(fileName);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return "success";
    }

    private String getAvailableFileName() {
        int counterFiles = 1;
        File f = new File(BASE_FILE_FOR_REQUESTS + counterFiles + ".json");
        while (f.exists()){
            counterFiles++;
            f = new File(BASE_FILE_FOR_REQUESTS + counterFiles + ".json");
        }
        return BASE_FILE_FOR_REQUESTS + counterFiles + ".json";
    }
}
