package com.aggregator.aggregator.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Data
public class Configuration {

//    private String protocol;
//    private Integer frequency;
//    private String status;
//    private String actuator;

    public String protocol;
    public String frequency;
    public String dataSource;
    public String config_location;
    public String url;
    public String topic;
    public String status;
}
