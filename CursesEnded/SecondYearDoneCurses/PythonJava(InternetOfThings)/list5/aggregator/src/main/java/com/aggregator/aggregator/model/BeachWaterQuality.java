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
public class BeachWaterQuality extends BaseEntity {

    @JsonProperty("Water Temperature")
    private double temp;

    @Override
    public String toString() {
        return "BeachWaterQuality{" +
                "temp=" + temp +
                '}';
    }
}
