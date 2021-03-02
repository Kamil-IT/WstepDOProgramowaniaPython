package com.example.demo;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Request {

    private List<String> students = new ArrayList<>();
    private String time;

    public Request() {
    }

    public Request(List<String> students, String time) {
        this.students = students;
        this.time = time;
    }

    public List<String> getStudents() {
        return students;
    }

    public void setStudents(List<String> students) {
        this.students = students;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Request)) return false;

        Request request = (Request) o;

        if (!Objects.equals(students, request.students)) return false;
        return Objects.equals(time, request.time);
    }

    @Override
    public int hashCode() {
        int result = students != null ? students.hashCode() : 0;
        result = 31 * result + (time != null ? time.hashCode() : 0);
        return result;
    }

    @Override
    public String toString() {
        return "Request{" +
                "students=" + students +
                ", time='" + time + '\'' +
                '}';
    }
}
