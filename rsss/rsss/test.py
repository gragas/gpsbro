from rsss.collector import Collector

def main():
    geonet_marks = Collector.get_geonet_marks("tsunami", "operational")
    for mark in geonet_marks:
        print(mark)

if __name__ == "__main__":
    main()
