#lots to do here

##[Unit11213]
##Name=NONE
##Direction=2
##NumAtoms=11
##NumCells=11
##UnitNumber=11213
##UnitType=3
##NumberBlocks=1
##
##[Unit11213_Block1]
##Name=SRS_LIKE26_s_at
##BlockNumber=1
##NumAtoms=11
##NumCells=11
##StartPosition=0
##StopPosition=10
##CellHeader=X	Y	PROBE	FEAT	QUAL	       EXPOS  	POS	CBASE	PBASE	TBASE	ATOM	INDEX	CODONIND	CODON	REGIONTYPE	REGION
##Cell1=403	355	N	control	SRS_LIKE26_s_at	0	13	C	G	C	0	170093	-1	-1	99	
##Cell2=185	69	N	control	SRS_LIKE26_s_at	1	13	A	T	A	1	33167	-1	-1	99	
##Cell3=27	62	N	control	SRS_LIKE26_s_at	2	13	C	G	C	2	29663	-1	-1	99	
##Cell4=420	10	N	control	SRS_LIKE26_s_at	3	13	T	A	T	3	5200	-1	-1	99	
##Cell5=155	29	N	
##
##X - The X coordinate of the cell.
##Y - The Y coordinate of the cell.
##PROBE - The probe sequence of the cell. Typically set to "N".
##FEAT - Unused string.
##QUAL - The same as the block name.
##EXPOS - Ranges from 0 to the number of atoms - 1 for expression arrays. For CustomSeq it provides some positional information for the probe.
##POS - An index to the base position within the probe where the mismatch occurs.
##CBASE - Not used.
##PBASE - The probe base at the substitution position.
##TBASE - The base of the target where the probe interrogates at the substitution position.
##ATOM - An index used to group probe pairs or quartets.
##INDEX - An index used to look up the corresponding cell data in the CEL file.
##CODONIND - Always set to -1. Only available in version 2 and above.
##CODON -Always set to -1. Only available in version 2 and above.
##REGIONTYPE - Always set to 99. Only available in version 2 and above.
##REGION - Always set to a blank character. Only available in version 2 and above.
##Celli	This con

class affycdf():
	def _int_(self, celldata, alltags):
		self.celldata = celldata
		self.alltags = {}
    
    read_tag = dict(inttype = int(rowpartition[2].strip()),
                    stringtype = str(rowpartition[2].strip()),
                    tupletype = tuple(row[1:])
                    )
    
    header_data_types =dict(X=int,
                            Y=int,
                            PROBE=str,
                            FEAT=str,
                            QUAL=str,
                            EXPOS=int,
                            POS=int,
                            CBASE=str,
                            PBASE=str,
                            TBASE=str,
                            ATOM=int,
                            INDEX=int,
                            CODONIND=str,
                            CODON=str,
                            REGIONTYPE=str,
                            REGION=str,
                            Celli=tuple,
                            PROB=str,
                            PLEN=int,
                            INDEX=int,
                            MATCH=bool,
                            BG=bool,
                            CYCLES=tuple,
                            )
                            
    def header_reader(header):
    	
    def read_data_row(row):
    		                        
    
    # some of he data elements appear in multiple section of the file. The definition for each is listed.
    ## If there is a different method needed to parse the two different occurances it is specified
    ##alltags=dict()
    
    #Version	The version number. Should always be set to "GC1.0", "GC2.0" or "GC3.0". This document only describes GC3.0 version CDF files.
    self.alltags['Version'] = read_tag['stringtype']
    #Type Defines the type of QC probe set. The defined types are:
    self.alltags['Type'] = read_tag['inttype']
    
    #NumCells	The number of cells in the block.
    self.alltags['NumberCells'] = read_tag['inttype']
    
    # [QC], CellHeader Defines the data contained in the subsequent lines, separated by tabs. The value depends on the type of unit. The possible values are:
    # [Unit] CellHeader	Defines the data contained in the subsequent lines, separated by tabs. The values are:
    self.alltags['CellHeader'] = header_reader
    self.alltags['Cell'] = read_data_row # Data rows start with "CELL" the number of colums is set by the header, Parsing is the same, /t seperated values
    
    # [CHIP], Name This item is not used by the software.
    # [UNIT], Name The name of the unit or "NONE" for expression units.
    # [Unit_Block],Name The name of the block. For expression units this is the name of the probe set.
    self.alltags['name'] = read_tag['stringtype']
    
    # Direction Defines if the probes are interrogating a sense target or anti-sense target (1 - sense, 2 - anti-sense).
    # Direction Defines if the probes are interrogating a sense target or anti-sense target (0 - no direction, 1 - sense, 2 - anti-sense).
    ##This value is available in version 3 and above.
    self.alltags['Direction'] = read_tag['inttype']
    
    #1, NumAtoms The number of atoms (probe pairs for expression and genotyping and probe quartets for CustomSeq) in the entire probe set.
    ##This TAG name contain two values after the equal sign. The first is the number of atoms and the second (if found) is the number of cells in each atom.
    ##It is assumed that there are 2 cells per atom for expression probe sets and 4 for CustomSeq probe sets.
    #2, NumAtoms The number of atoms (probe pairs for expression and genotyping and probe quartets for CustomSeq) in the block.
    self.alltags['NumAtoms'] = read_tag['inttype']
    
    #NumCells The number of cells in the entire probe set.
    self.alltags['NumCells'] = read_tag['inttype']
    
    #StartPosition The position of the first atom.
    self.alltags['StartPosition'] = read_tag['inttype']
    
    #StopPosition The position of the last atom.
    self.alltags['StopPosition'] = read_tag['inttype']
    
    #UnitNumber	An arbitrary index value for the probe set.
    self.alltags['UnitNumber'] = read_tag['inttype']
    
    #UnitType Defines the type of unit (1 - CustomSeq, 2 - genotyping, 3 - expression, 7 - tag/GenFlex).
    self.alltags['UnitType'] = read_tag['inttype']
    
    #NumberBlocks The number of blocks or groups in the probe set.
    self.alltags['NumberBlocks'] = read_tag['inttype']
    
    #MutationType Used for CYP450 arrays only in defining the type of polymorphism (0 - substitution, 1 - insertion, 2 - deletion).
    ##This value is available in version 2 and above and only if the UnitType=2.
    self.alltags['MutationType'] = read_tag['inttype']
    
    #BlockNumber An index to the block.
    self.alltags['BlockNumber'] = read_tag['inttype']
    
    #Rows The number of rows of cells on the array.
    self.alltags['Rows'] = read_tag['inttype']
    
    #Cols The number of columns of cells on the array.
    self.alltags['Cols'] = read_tag['inttype']
    
    #NumberOfUnits The number of units in the array not including QC units. The term unit is an internal term which means probe set.
    self.alltags['NumberOfUnits'] = read_tag['inttype']
    
    #MaxUnit Each unit is given a unique number. This value is the maximum of the unit numbers of all the units in the array (not including QC units).
    self.alltags['MaxUnit'] = read_tag['inttype']
    
    #NumQCUnits	The number of QC units. QC units are defined in version 2 and above.
    self.alltags['NumQCUnits'] = read_tag['inttype']
    
    #ChipReference Used for CustomSeq, HIV and P53 arrays only. This is the reference sequence displayed by the Affymetrix software.
    ##The sequence may contain spaces. This value is defined for version 2 and above.
    self.alltags['ChipReference'] = read_tag['tupletype']
    
    #The CDF file describes the layout for an Affymetrix GeneChip array. There are two formats of this file --
    ##the first is an ASCII text format used by the MAS and GCOS 1.0 software and the second is a binary format used by later versions of GCOS - this format is also referred to as the XDA format.
    self.alltags['CDF']= section_reader(row, '[CDF]')
    
    #The "Chip" section
    self.alltags['Chip']= section_reader(row, '[Chip]')
    
    #"QC" defines the QC units or probe sets in the array. There are NumQCUnits (from the Chip section) QC sections. 
    ##Each section name is a combination of "QC" and an index ranging from 1 to NumQCUnits-1. QC units are defined for version 2 and above.
    self.alltags['QC'] = section_reader(row, 'QC')
    
    #"Unit" defines the probes that are a member of the unit (probe set).
    ##Each probe set is divided into subsections termed "Blocks" which are referred to as "groups" in the Files SDK documentation.
    ##A group will list the probes as its members. For expression probe sets there is 1 and only 1 group per probe set.
    ##Each section name is a combination of "Unit" and an index. There is no meaning to the index value.
    ##Immediately following the "Unit" section there will be the "Block" sections for that unit before the next unit is defined.
    self.alltags['Unit'] = section_reader(row, '[Unit]')
    
    #There are as many "Unit_Block" sections as defined in the "Unit" section.
    ##Removed becuase it is inclueded in reading in the "Unit" data
    ##alltags['Unit_Block'] = section_reader(row, '[Unit_Block]')
                
    def section_reader(row, section):
        if section == 'CDF':
            row = reader.next()
            self.alltags[str(row)] == alltags[str(row)](row)
        elif sectionn == 'Chip':
        	row = reader.next()
        	self.alltags[str(row)] == alltags[str(row)](row)
        elif section == 'QC':
        	row = reader.next()
        	self.alltags[str(row)] == alltags[str(row)](row)
        elif section == 'Unit':
        	row = reader.next()
        	self.alltags[str(row)] == alltags[str(row)](row)
    
    def read_cdf(self, file):
        reader = csv.reader(open(filename, "U"),delimiter='\t')
        self.filename = os.path.split(filename)[1]
        for row in reader:
            if row: #skip blank rows
                alltags[row[0].partition('=').strip(' []1234567890] ')[0]](row) #Looks up the correct way to read the line based on the tag. This work for all line, ie if there is no "=" no error is raised                         
        rows =[]
        for row in range(NumCells):
            rows.append(tuple(row))
            self.celldata = np.array(rows, [(col,row_data_type[str(col)] for col in CellHeader)])
            
            
    
        
    
        
