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
public class Temperature extends BaseEntity {

    private Double temp;
    @JsonProperty("outside/inside")
    private String outside_inside;

    @Override
    public String toString() {
        return "Temperature{" +
                "temp=" + temp +
                ", outside_inside='" + outside_inside + '\'' +
                '}';
    }
}
