data = {
"region": {
"name": "Africa",
"avgAge": 19.7,
"avgDailyIncomeInUSD": 5,
"avgDailyIncomePopulation": 0.71
},
"periodType": "days",
"timeToElapse": 58,
"reportedCases": 674,
"population": 66622705,
"totalHospitalBeds": 1380614
}
def estimator(data):
    def impact():
        currentlyInfected = int(data["reportedCases"] * 10)
        #currentlyInfecteds = {"CurrentlyInfected": currentlyInfected}
        setattr(impact, 'currentlyInfected', currentlyInfected)
  

        numberOf3DaysIn58Days = data["timeToElapse"] / 3
        numberOf3DaysIn58Days = int(numberOf3DaysIn58Days)
        infectionsByRequestedTime = int(currentlyInfected * (2**numberOf3DaysIn58Days))
        #infectionsByRequestedTimes = {"InfectionsByRequestedTime": infectionsByRequestedTime}
        setattr(impact, 'infectionsByRequestedTime', infectionsByRequestedTime)

        severeCasesByRequestedTime = (15/100) * infectionsByRequestedTime
        severeCasesByRequestedTime = int(severeCasesByRequestedTime)
        #severeCasesByRequestedTimes = {"SevereCasesByRequestedTime": severeCasesByRequestedTime}
        setattr(impact, 'severeCasesByRequestedTime', severeCasesByRequestedTime)

        availableBeds = (35/100) * data["totalHospitalBeds"]
        availableBeds = int(availableBeds)
        hospitalBedsByRequestedTime = severeCasesByRequestedTime - availableBeds
        #hospitalBedsByRequestedTimes = {"HospitalBedsByRequestedTime": hospitalBedsByRequestedTime}
        setattr(impact, 'hospitalBedsByRequestedTime', hospitalBedsByRequestedTime)

        casesForICUByRequestedTime = (5/100) * infectionsByRequestedTime
        casesForICUByRequestedTime = int(casesForICUByRequestedTime)
        #casesForICUByRequestedTimes = {"CasesForICUByRequestedTime": casesForICUByRequestedTime}
        setattr(impact, 'casesForICUByRequestedTime', casesForICUByRequestedTime)

        casesForVentilatorsByRequestedTime = (2/100) * infectionsByRequestedTime
        casesForVentilatorsByRequestedTime = int(casesForVentilatorsByRequestedTime)
        #casesForVentilatorsByRequestedTimes = {"CasesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTime}
        setattr(impact, 'casesForVentilatorsByRequestedTime', casesForVentilatorsByRequestedTime)

        dollarsInFlight = (infectionsByRequestedTime * data["region"]["avgDailyIncomeInUSD"]) / data["timeToElapse"]
        dollarsInFlight = int(dollarsInFlight)
        #dollarsInFlights = {"DollarsInFlight": dollarsInFlight}
        setattr(impact, 'dollarsInFlight', dollarsInFlight)

        output = {"CurrentlyInfected": impact.currentlyInfected, "InfectionsByRequestedTime":impact.infectionsByRequestedTime, "SevereCasesByRequestedTime": impact.severeCasesByRequestedTime,
        "HospitalBedsByRequestedTime": impact.hospitalBedsByRequestedTime, "CasesForICUByRequestedTime": impact.casesForICUByRequestedTime, "CasesForVentilatorsByRequestedTime": impact.casesForVentilatorsByRequestedTime, "DollarsInFlight": impact.dollarsInFlight}
       
        return (output)
    #impact()
    def severeImpact():
        currentlyInfected = int(data["reportedCases"] * 50)
        #currentlyInfecteds = {"CurrentlyInfected": currentlyInfected}
        setattr(severeImpact, 'currentlyInfected', currentlyInfected)
  

        numberOf3DaysIn58Days = data["timeToElapse"] / 3
        numberOf3DaysIn58Days = int(numberOf3DaysIn58Days)
        infectionsByRequestedTime = int(currentlyInfected * (2**numberOf3DaysIn58Days))
        #infectionsByRequestedTimes = {"InfectionsByRequestedTime": infectionsByRequestedTime}
        setattr(severeImpact, 'infectionsByRequestedTime', infectionsByRequestedTime)

        severeCasesByRequestedTime = (15/100) * infectionsByRequestedTime
        severeCasesByRequestedTime = int(severeCasesByRequestedTime)
        #severeCasesByRequestedTimes = {"SevereCasesByRequestedTime": severeCasesByRequestedTime}
        setattr(severeImpact, 'severeCasesByRequestedTime', severeCasesByRequestedTime)

        availableBeds = (35/100) * data["totalHospitalBeds"]
        availableBeds = int(availableBeds)
        hospitalBedsByRequestedTime = severeCasesByRequestedTime - availableBeds
        #hospitalBedsByRequestedTimes = {"HospitalBedsByRequestedTime": hospitalBedsByRequestedTime}
        setattr(severeImpact, 'hospitalBedsByRequestedTime', hospitalBedsByRequestedTime)

        casesForICUByRequestedTime = (5/100) * infectionsByRequestedTime
        casesForICUByRequestedTime = int(casesForICUByRequestedTime)
        #casesForICUByRequestedTimes = {"CasesForICUByRequestedTime": casesForICUByRequestedTime}
        setattr(severeImpact, 'casesForICUByRequestedTime', casesForICUByRequestedTime)

        casesForVentilatorsByRequestedTime = (2/100) * infectionsByRequestedTime
        casesForVentilatorsByRequestedTime = int(casesForVentilatorsByRequestedTime)
        #casesForVentilatorsByRequestedTimes = {"CasesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTime}
        setattr(severeImpact, 'casesForVentilatorsByRequestedTime', casesForVentilatorsByRequestedTime)

        dollarsInFlight = (infectionsByRequestedTime * data["region"]["avgDailyIncomeInUSD"]) / data["timeToElapse"]
        dollarsInFlight = int(dollarsInFlight)
        #dollarsInFlights = {"DollarsInFlight": dollarsInFlight}
        setattr(severeImpact, 'dollarsInFlight', dollarsInFlight)

        output = {"CurrentlyInfected": severeImpact.currentlyInfected, "InfectionsByRequestedTime":severeImpact.infectionsByRequestedTime, "SevereCasesByRequestedTime": severeImpact.severeCasesByRequestedTime,
        "HospitalBedsByRequestedTime": severeImpact.hospitalBedsByRequestedTime, "CasesForICUByRequestedTime": severeImpact.casesForICUByRequestedTime, "CasesForVentilatorsByRequestedTime": severeImpact.casesForVentilatorsByRequestedTime,
        "DollarsInFlight": severeImpact.dollarsInFlight}
        return output
        #print("severeImpact:" + str(output))
    #severeImpact()
    output = {"data": data, "impact": impact(), "severeImpact": severeImpact()}
    print(output)
estimator(data)