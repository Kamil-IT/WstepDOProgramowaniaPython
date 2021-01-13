package com.aggregator.aggregator.converter;

import java.util.Date;

public class DataConverter {

    public static Date getDataFromString(String date, String time){
        return new Date(
                Integer.parseInt(date.substring(0, 4)) - 1900,
                Integer.parseInt(date.substring(5, 7)) - 1,
                Integer.parseInt(date.substring(8, 10)),
                Integer.parseInt(time.substring(0, 2)) - 1,
                Integer.parseInt(time.substring(3, 5))
        );
    }
}
