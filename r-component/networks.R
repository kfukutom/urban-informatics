libraries <- c(
  "tidyverse", "sf",
  "giscorR", "httr",
  "XML", "osmdata",
  "ggplot2"
)

installed_libs <- libraries %in% rownames(install.packages())
if (any(installed_libs == FALSE)) {
  install.packages(libraries[!installed_libs])
}

invisible(lapply(libraries, library, character.only=TRUE))

#Chicago's Road Network (1)
bbox <- getbb("Chicago, Illinois", format_out="matrix")
query <- opq(bbox = bbox) %>%
  add_osm_feature(key="highway")
road_data <- osmdata_sf(query)

highways <- road_data$osm_lines %>%
  filter(highway %in% c("motorway", "trunk"))

other_roads <- road_data$osm_lines %>% 
  filter(!(highway %in% c("motorway", "trunk")))

ggplot() + 
  geom_sf(data=other_roads, color="grey", size=0.12) +
  geom_sf(data=highways, color="yellow", size=0.5) +
  theme_minimal() + 
  labs(title = "Advanced Road Map of Chicago, Illinois") +
  theme(axis.text = element_text(size = 12),
        axis.title = element_text(size = 14),
        plot.title = element_text(size = 20, face = "bold"))

ggsave("advanced_road_network_CH", width=16, height=9)


q <- opq(bbox = getbb("Chicago, IL"))
plot_area <- c(-87.94009, 41.64453, -87.52408, 42.02304)
# query
college_feature <- plot_area %>%
  opq(timeout = 25*100) %>%
  add_osm_feature(key="amenity",
                  value = c("college"))
college_density <- osmdata_sf(college_feature)
print(college_density)

?geom_sf

ggplot() +
  geom_sf(data=college_density$osm_points,
          inherit.aes = FALSE,
          color = "#FFFF33",
          size = 0.1,
          alpha = 0.8)

