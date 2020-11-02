package com.aggregator.aggregator.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class BeachWaterQuality extends DateDelivery {

    @JsonProperty("Water Temperature")
    private double temp;
//
//    @JsonProperty("Water Temperature")
//    public double getTemp() {
//        return temp;
//    }
//
//    @JsonProperty("Water Temperature")
//    public void setTemp(double temp) {
//        this.temp = temp;
//    }
}
