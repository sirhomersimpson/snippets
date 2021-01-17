package com.udemy.dropbookmarks.resources;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import java.awt.*;

@Path("/greeting")
public class HelloResource {

    @GET
    @Produces(MediaType.TEXT_HTML)
    public String getGreeting() {
        return "<b>Hello Rikesh2<b>";
    }
}
