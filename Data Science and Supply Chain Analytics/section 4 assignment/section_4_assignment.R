cars_file<-read.csv('cars.csv')

head(cars_file,5)

summary(cars_file)

matrix(cars_file)

num_rows<-nrow(cars_file)
num_col<-ncol(cars_file)
dim_df<-dim(cars_file)
len_df<-length(cars_file)

unique_num_cylinders <- unique(cars_file$cylinders)

names(cars_file)[names(cars_file) == 'name'] <- 'car name'

car_pricing <- cars_file[c(1,9)]

pricing_category <- function(price){
  
  if(price <= 20000){ 
    "Budget Car "
  } else if (price <= 35000 ){
    "Suitable Car"
  } else {
    "Expensive Car"
  }
}

pricing_category(30000)
pricing_category(20000)
price_category(50000)

car_pricing$Price[1]

for (i in 1: length(car_pricing)){
  
  car_pricing$category[i]<- price_category(car_pricing$Price[i])
}



head(car_pricing)

summary(car_pricing)
table(car_pricing$category)



