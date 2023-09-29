import proj4 from "proj4";

// EPSG:5181 정의
const epsg5181 = "+proj=tmerc +lat_0=38 +lon_0=127.5 +k=0.9996 +x_0=200000 +y_0=500000 +ellps=GRS80 +units=m +no_defs";

// WGS84 정의
const wgs84 = "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs";

// 변환할 좌표
const x = 344434.54990000185;
const y = 576946.74580000155;

// EPSG:5181에서 WGS84로 변환
const [lon, lat] = proj4(epsg5181, wgs84, [x, y]);

console.log(`Longitude: ${lon}, Latitude: ${lat}`);
