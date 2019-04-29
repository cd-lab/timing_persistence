readTimingdata <- function(fname="allParticipant.csv"){
  Timingrawdata <<- read.csv(fname)
  # This is an array with each subjects' ``name''
  Timingsubjects <<- unique(Timingrawdata$participant)
  # This is an integer with the number of participants
  Timingnsub <<- length(Timingsubjects)
  # This list holds each participants' data.  It has Timingnsub entries
  Timingdatalist <<- vector("list", Timingnsub)
  for(i in 1:Timingnsub){
    inds <- Timingrawdata$participant == Timingsubjects[i]
    Timingdatalist[[i]] <<- Timingrawdata[inds,]
  }
}


excludeFast <- function(){
  table <- Timingrawdata[1,]
  for(i in 2:length(Timingrawdata$rtRound1_3.rt)){
    if(is.na(Timingrawdata$rtRound1_3.rt[i])==FALSE & Timingrawdata$rtRound1_3.rt[i]>0.15){
      table <- rbind(table,Timingrawdata[i,])
    }
  }
  return(table)
}
  
setCondition <- function(){
  for(i in 1:length(table$rtRound1_3.rt)){
    table$condition[i]<-(table$firstTime[i]+10*table$secondTime[i])
  }
  return(table)
}

conditonAccuracy <- function(){
  conditions<-unique(table1$condition)
  conCorrect<-array(0, c(1,length(conditions)))
  num<-array(0,c(1,length(conditions)))
  totalRT<-array(0,c(1,length(conditions)))
  for(i in 1:length(table1$rtRound1_3.rt)){
    for(ii in 1:length(conditions)){
      if(table1$condition[i]==conditions[ii]){
        conCorrect[ii]<-conCorrect[ii]+table1$rtRound1_3.corr[i]
        num[ii]<-num[ii]+1
        totalRT[ii]<-totalRT[ii]+table1$rtRound1_3.rt[i]
      }
    }
  }
  acc<-rbind(conditions,conCorrect,num,totalRT)
  return(acc)
}
  

hi<-function(){
  k<-array(NaN,c(2,10))
  for(i in 1:length(dataAll$Condition)){
    a<-1
    b<-1
    if(dataAll$ratio[i]<1){
      k[1,a]<-dataAll$Average.Accuracy
      a<-a+1
    }
    if(dataAll$ratio[i]>=1){
      k[2,b]<-dataAll$Average.Accuracy
      b<-b+1
    }
  }
  return(k)
}
  



individualScore <- function(sub=1) {
  subdata <- Timingdatalist[[sub]]
  subID <- subdata$participant[1]
  numTrial <- length(subdata$firstTime)
  subMeanAcc <- mean(subdata$rtRound1_3.corr)
  subMeanRT <- mean(subdata$rtRound1_3.rt)
  array<-c(subID,numTrial,subMeanAcc,subMeanRT)
  return(array)
}


allScores<- function(){
  table<-individualScore(1)
  for (i in 2:length(Timingdatalist)){
    table<-rbind(table,individualScore(i))
  }
  return(table)
}




















