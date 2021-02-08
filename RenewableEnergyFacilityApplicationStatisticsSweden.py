
renewSweStatSchema2 = 'SiteName:STRING,OrgID:STRING,Company:STRING,Shares:STRING,AllocationPct:STRING,' \
                     'InitialCapacity:INTEGER,ExpectedElectricityCertCapacity:INTEGER,InstalledCapacity:INTEGER,' \
                     'EnergySource:String,Type:STRING,ElectricityRegion:STRING,ExpiryDate:DATE,'


"""
Förklaring av kolumner	

Anläggningens namn |	Namn på anläggningen

Organisationsnr |	Organisationsnummer för innehavaren av anläggningen. För anläggningar som ägs av privatpersoner anges "Privatperson" istället för personnummer

Företagsnamn |	Namn på innehavaren av anläggningen. För anläggningar som ägs av privatpersoner anges "Privatperson" istället för namn.

Innehav |	Visar antalet innehavare för anläggningen

Tilldelningsfaktor (%) |	Den procentuella andel av anläggningens produktion som är berättigad till elcertifikat.  Anläggningar som är godkända för sin fullständiga produktion har 100 % i kolumnen. Anläggningar godkända för produktionsökning har tilldelningsfaktor mellan 0 och 100 %. Vattenanläggningar utan tilldelningsfaktor månadsdeklarerar, vilket innebär att inte samtliga enheter berättigar till elcertifikat.  Anläggningar som har produktionsenheter av olika energikällor månadsdeklarerar också. Dessa anläggningars tilldelningsfaktorer framgår inte i kolumnen

Vid ansökan angiven normalårsproduktion (MWh) |	Den beräknade årliga produktionen av förnybar el vid normala driftförhållanden som innehavaren angett i ansökan

Förväntad elcertifikatberättigad produktion (MWh) |	"Tilldelningsfaktorn multiplicerat med normalårsproduktionen ger den förväntade elcertifikatberättigade produktionen. 
För vattenanläggningar utan tilldelningsfaktor räknas inte den förväntade elcertifikatproduktionen ut."

Installerad effekt (kW) |	Den installerade effekten som anläggningens generator har. Om anläggningen inte har en generator anges den installerade eleffekten

Energikälla |	Den energikälla som används i anläggningen

Typ	| En mer detaljerad beskrivning av energikälla. För vatten- och biokraftanläggningar som har utfört produktionsökningar och fått en bestämd andel av produktionen godkänd för tilldelning av elcertifikat anges "Produktionsökning"

Nätområdes-ID |	Det nätområdes-ID som anläggningen har

Elområde |	Det elområde där anläggningen finns

Slutdatum för tilldelning |	Anläggningens slutdatum för tilldelning av elcertifikat (i den aktuella tilldelningsperioden)

Vid ansökan angivet 
drifttagningsdatum produktionsenhet (vid flera enheter anges drifttagningsdatum för första och sista enhet) |	Det/de drifttagningsdatum som angivits vid ansökan

Beslutstyp |	Den typ av beslut som fattats för anläggningen. Följande alternativ finns: 1) Ny anläggning 2) Ny tilldelning efter omfattande ombyggnad 3) Ny tilldelning efter produktionsökning

Antal produktionsenheter bakom anläggningens mätpunkt |	Det antal produktionsenheter som finns bakom anläggningens mätpunkt

Ort |	Den ort där anläggingen finns

Kommun |	Den kommun där anläggningen finns

Län |	Det län där anläggningen finns

Huvudvattendrag |	För vattenkraftanläggningar anges det vattendrag där anläggningen finns
"""