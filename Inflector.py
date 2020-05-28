#coding: utf8 

import re

"""
/**
 * @class Inflector
 */
"""
class Inflector (object):
	# the cache store for later use
	_cacheStore = {}
	
	# the plural rules
	_plural = {
		'rulesOrderedKeys': [
			r'(s)tatus$',
			r'(quiz)$',
			r'^(ox)$',
			r'([m|l])ouse$',
			r'(matr|vert|ind)(ix|ex)$',
			r'(x|ch|ss|sh)$',
			r'([^aeiouy]|qu)y$',
			r'(hive)$',
			r'(?:([^f])fe|([lre])f)$',
			r'sis$',
			r'([ti])um$',
			r'(p)erson$',
			r'(m)an$',
			r'(c)hild$',
			r'(buffal|tomat)o$',
			r'(alumn|bacill|cact|foc|fung|nucle|radi|stimul|syllab|termin|vir)us$',
			r'us$',
			r'(alias)$',
			r'(ax|cris|test)is$',
			r's$',
			r'^$',
			r'$'
		],
		'rules': {
			r'(s)tatus$' : r'\1tatuses',
			r'(quiz)$' : r'\1zes',
			r'^(ox)$' : r'\1\2en',
			r'([m|l])ouse$' : r'\1ice',
			r'(matr|vert|ind)(ix|ex)$' : r'\1ices',
			r'(x|ch|ss|sh)$' : r'\1es',
			r'([^aeiouy]|qu)y$' : r'\1ies',
			r'(hive)$' : r'\1s',
			r'(?:([^f])fe|([lre])f)$' : r'\1\2ves',
			r'sis$' : r'ses',
			r'([ti])um$' : r'\1a',
			r'(p)erson$' : r'\1eople',
			r'(m)an$' : r'\1en',
			r'(c)hild$' : r'\1hildren',
			r'(buffal|tomat)o$' : r'\1\2oes',
			r'(alumn|bacill|cact|foc|fung|nucle|radi|stimul|syllab|termin|vir)us$' : r'\1i',
			r'us$' : r'uses',
			r'(alias)$' : r'\1es',
			r'(ax|cris|test)is$' : r'\1es',
			r's$' : r's',
			r'^$' : r'',
			r'$' : r's'
		},
		'uninflected': [
			r'.*[nrlm]ese', r'.*deer', r'.*fish', r'.*measles', r'.*ois', r'.*pox', r'.*sheep', r'people', r'feedback'
		],
		'irregular': {
			r'atlas' : r'atlases',
			r'beef' : r'beefs',
			r'brief' : r'briefs',
			r'brother' : r'brothers',
			r'cafe' : r'cafes',
			r'child' : r'children',
			r'cookie' : r'cookies',
			r'corpus' : r'corpuses',
			r'cow' : r'cows',
			r'ganglion' : r'ganglions',
			r'genie' : r'genies',
			r'genus' : r'genera',
			r'graffito' : r'graffiti',
			r'hoof' : r'hoofs',
			r'loaf' : r'loaves',
			r'man' : r'men',
			r'money' : r'monies',
			r'mongoose' : r'mongooses',
			r'move' : r'moves',
			r'mythos' : r'mythoi',
			r'niche' : r'niches',
			r'numen' : r'numina',
			r'occiput' : r'occiputs',
			r'octopus' : r'octopuses',
			r'opus' : r'opuses',
			r'ox' : r'oxen',
			r'penis' : r'penises',
			r'person' : r'people',
			r'sex' : r'sexes',
			r'soliloquy' : r'soliloquies',
			r'testis' : r'testes',
			r'trilby' : r'trilbys',
			r'turf' : r'turfs',
			r'potato' : r'potatoes',
			r'hero' : r'heroes',
			r'tooth' : r'teeth',
			r'goose' : r'geese',
			r'foot' : r'feet'
		}
	}
	
	# singular rules
	_singular = {
		'rulesOrderedKeys': [
			r'(s)tatuses$',
			r'^(.*)(menu)s$',
			r'(quiz)zes$',
			r'(matr)ices$',
			r'(vert|ind)ices$',
			r'^(ox)en',
			r'(alias)(es)*$',
			r'(alumn|bacill|cact|foc|fung|nucle|radi|stimul|syllab|termin|viri?)i$',
			r'([ftw]ax)es',
			r'(cris|ax|test)es$',
			r'(shoe)s$',
			r'(o)es$',
			r'ouses$',
			r'([^a])uses$',
			r'([m|l])ice$',
			r'(x|ch|ss|sh)es$',
			r'(m)ovies$',
			r'(s)eries$',
			r'([^aeiouy]|qu)ies$',
			r'(tive)s$',
			r'(hive)s$',
			r'(drive)s$',
			r'([le])ves$',
			r'([^rfoa])ves$',
			r'(^analy)ses$',
			r'(analy|diagno|^ba|(p)arenthe|(p)rogno|(s)ynop|(t)he)ses$',
			r'([ti])a$',
			r'(p)eople$',
			r'(m)en$',
			r'(c)hildren$',
			r'(n)ews$',
			r'eaus$',
			r'^(.*us)$',
			r's$'
		],
		'rules': {
			r'(s)tatuses$' : r'\1tatus',
			r'^(.*)(menu)s$' : r'\1\2',
			r'(quiz)zes$' : r'\1',
			r'(matr)ices$' : r'\1ix',
			r'(vert|ind)ices$' : r'\1ex',
			r'^(ox)en' : r'\1',
			r'(alias)(es)*$' : r'\1',
			r'(alumn|bacill|cact|foc|fung|nucle|radi|stimul|syllab|termin|viri?)i$' : r'\1us',
			r'([ftw]ax)es' : r'\1',
			r'(cris|ax|test)es$' : r'\1is',
			r'(shoe)s$' : r'\1',
			r'(o)es$' : r'\1',
			r'ouses$' : r'ouse',
			r'([^a])uses$' : r'\1us',
			r'([m|l])ice$' : r'\1ouse',
			r'(x|ch|ss|sh)es$' : r'\1',
			r'(m)ovies$' : r'\1\2ovie',
			r'(s)eries$' : r'\1\2eries',
			r'([^aeiouy]|qu)ies$' : r'\1y',
			r'(tive)s$' : r'\1',
			r'(hive)s$' : r'\1',
			r'(drive)s$' : r'\1',
			r'([le])ves$' : r'\1f',
			r'([^rfoa])ves$' : r'\1fe',
			r'(^analy)ses$' : r'\1sis',
			r'(analy|diagno|^ba|(p)arenthe|(p)rogno|(s)ynop|(t)he)ses$' : r'\1\2sis',
			r'([ti])a$' : r'\1um',
			r'(p)eople$' : r'\1\2erson',
			r'(m)en$' : r'\1an',
			r'(c)hildren$' : r'\1\2hild',
			r'(n)ews$' : r'\1\2ews',
			r'eaus$' : r'eau',
			r'^(.*us)$' : r'\\1',
			r's$' : r''
		},
		'uninflected': [
			r'.*[nrlm]ese', r'.*deer', r'.*fish', r'.*measles', r'.*ois', r'.*pox', r'.*sheep', r'.*ss', r'feedback'
		],
		'irregular': {
			r'foes' : r'foe'
		}
	}
	
	# words that should not be inflected
	_uninflected = [
		'Amoyese', 'bison', 'Borghese', 'bream', 'breeches', 'britches', 'buffalo', 'cantus',
		'carp', 'chassis', 'clippers', 'cod', 'coitus', 'Congoese', 'contretemps', 'corps',
		'debris', 'diabetes', 'djinn', 'eland', 'elk', 'equipment', 'Faroese', 'flounder',
		'Foochowese', 'gallows', 'Genevese', 'Genoese', 'Gilbertese', 'graffiti',
		'headquarters', 'herpes', 'hijinks', 'Hottentotese', 'information', 'innings',
		'jackanapes', 'Kiplingese', 'Kongoese', 'Lucchese', 'mackerel', 'Maltese', '.*?media',
		'metadata', 'mews', 'moose', 'mumps', 'Nankingese', 'news', 'nexus', 'Niasese',
		'Pekingese', 'Piedmontese', 'pincers', 'Pistoiese', 'pliers', 'Portuguese',
		'proceedings', 'rabies', 'rice', 'rhinoceros', 'salmon', 'Sarawakese', 'scissors',
		'sea[- ]bass', 'series', 'Shavese', 'shears', 'siemens', 'species', 'swine', 'testes',
		'trousers', 'trout', 'tuna', 'Vermontese', 'Wenchowese', 'whiting', 'wildebeest',
		'Yengeese'
	]
	
	# default map of accented and special characters to ASCII characters
	_transliteration = {
		r'À|Á|Â|Ã|Å|Ǻ|Ā|Ă|Ą|Ǎ' : r'A',
		r'Æ|Ǽ' : r'AE',
		r'Ä' : r'Ae',
		r'Ç|Ć|Ĉ|Ċ|Č' : r'C',
		r'Ð|Ď|Đ' : r'D',
		r'È|É|Ê|Ë|Ē|Ĕ|Ė|Ę|Ě' : r'E',
		r'Ĝ|Ğ|Ġ|Ģ|Ґ' : r'G',
		r'Ĥ|Ħ' : r'H',
		r'Ì|Í|Î|Ï|Ĩ|Ī|Ĭ|Ǐ|Į|İ|І' : r'I',
		r'Ĳ' : r'IJ',
		r'Ĵ' : r'J',
		r'Ķ' : r'K',
		r'Ĺ|Ļ|Ľ|Ŀ|Ł' : r'L',
		r'Ñ|Ń|Ņ|Ň' : r'N',
		r'Ò|Ó|Ô|Õ|Ō|Ŏ|Ǒ|Ő|Ơ|Ø|Ǿ' : r'O',
		r'Œ' : r'OE',
		r'Ö' : r'Oe',
		r'Ŕ|Ŗ|Ř' : r'R',
		r'Ś|Ŝ|Ş|Ș|Š' : r'S',
		r'ẞ' : r'SS',
		r'Ţ|Ț|Ť|Ŧ' : r'T',
		r'Þ' : r'TH',
		r'Ù|Ú|Û|Ũ|Ū|Ŭ|Ů|Ű|Ų|Ư|Ǔ|Ǖ|Ǘ|Ǚ|Ǜ' : r'U',
		r'Ü' : r'Ue',
		r'Ŵ' : r'W',
		r'Ý|Ÿ|Ŷ' : r'Y',
		r'Є' : r'Ye',
		r'Ї' : r'Yi',
		r'Ź|Ż|Ž' : r'Z',
		r'à|á|â|ã|å|ǻ|ā|ă|ą|ǎ|ª' : r'a',
		r'ä|æ|ǽ' : r'ae',
		r'ç|ć|ĉ|ċ|č' : r'c',
		r'ð|ď|đ' : r'd',
		r'è|é|ê|ë|ē|ĕ|ė|ę|ě' : r'e',
		r'ƒ' : r'f',
		r'ĝ|ğ|ġ|ģ|ґ' : r'g',
		r'ĥ|ħ' : r'h',
		r'ì|í|î|ï|ĩ|ī|ĭ|ǐ|į|ı|і' : r'i',
		r'ĳ' : r'ij',
		r'ĵ' : r'j',
		r'ķ' : r'k',
		r'ĺ|ļ|ľ|ŀ|ł' : r'l',
		r'ñ|ń|ņ|ň|ŉ' : r'n',
		r'ò|ó|ô|õ|ō|ŏ|ǒ|ő|ơ|ø|ǿ|º' : r'o',
		r'ö|œ' : r'oe',
		r'ŕ|ŗ|ř' : r'r',
		r'ś|ŝ|ş|ș|š|ſ' : r's',
		r'ß' : r'ss',
		r'ţ|ț|ť|ŧ' : r't',
		r'þ' : r'th',
		r'ù|ú|û|ũ|ū|ŭ|ů|ű|ų|ư|ǔ|ǖ|ǘ|ǚ|ǜ' : r'u',
		r'ü' : r'ue',
		r'ŵ' : r'w',
		r'ý|ÿ|ŷ' : r'y',
		r'є' : r'ye',
		r'ї' : r'yi',
		r'ź|ż|ž' : r'z'
	}
	
	"""
	/**
	 * @method _cache
	 * Sets a variable cache so that the Inflector class
	 * does not overwork as some of the methods are heavy.
	 *
	 * @param str type The type of alteration on the string
	 * @param str key The key (original word) to reference
	 * @param mixed value The value of the alteration performed on the string
	 *
	 * @return mixed
	 * @author Patrick K
	 */
	"""
	@staticmethod
	def _cache(type, key, value = None):
		key = '_' + str(key)
		type = '_' + str(type)
		if value is not None:
			# check for type in cache
			if type not in Inflector._cacheStore:
				Inflector._cacheStore[type] = {}
			# add value to cache
			Inflector._cacheStore[type][key] = value
			return value
		# for some reason the cache was not found, return nothing
		if type not in Inflector._cacheStore or key not in Inflector._cacheStore[type]:
			return None
		return Inflector._cacheStore[type][key]
	
	"""
	/**
	 * @method reset
	 * Does a simple reset of the cache of the Inflector class.
	 *
	 * @return void
	 * @author Patrick K
	 */
	"""
	@staticmethod
	def reset():
		Inflector._cacheStore = {}
	
	"""
	/**
	 * @method pluralize
	 * Return word in plural form.
	 *
	 * @param string word The word in singular form
	 *
	 * @return string
	 * @author Patrick K
	 */
	"""
	@staticmethod
	def pluralize(word):
		# just to be sure
		word = str(word)
		
		# get cache and check the return
		pluralCache = Inflector._cache('pluralize', word)
		if pluralCache is not None:
			return pluralCache
			
		# check for merged
		if 'merged' not in Inflector._plural:
			Inflector._plural['merged'] = {}
		# check for merged irregular
		if 'irregular' not in Inflector._plural['merged']:
			Inflector._plural['merged']['irregular'] = Inflector._plural['irregular']
		# check for merged uninflectored
		if 'uninflected' not in Inflector._plural['merged']:
			Inflector._plural['merged']['uninflected'] = Inflector._plural['uninflected']
			
		# check for plural caches
		if 'cacheUninflected' not in Inflector._plural or 'cacheIrregular' not in Inflector._plural:
			Inflector._plural['cacheUninflected'] = '(?:' + '|'.join(Inflector._plural['merged']['uninflected']) + ')'
			Inflector._plural['cacheIrregular'] = '(?:' + '|'.join(Inflector._plural['merged']['irregular'].keys()) + ')'
		
		# search for irregular string
		irregularMatches = re.findall('(.*)\\b(' + Inflector._plural['cacheIrregular'] + ')$', word, re.IGNORECASE)
		if len(irregularMatches) > 0:
			Inflector._cache('pluralize', word, Inflector._plural['merged']['irregular'][irregularMatches[-1][-1]])
			return Inflector._cache('pluralize', word)
			
		# search for uninflectable string
		uninflectedMatches = re.findall('^(' + Inflector._plural['cacheUninflected'] + ')$', word, re.IGNORECASE)
		if len(uninflectedMatches) > 0:
			Inflector._cache('pluralize', word, word)
			return Inflector._cache('pluralize', word)
			
		# run through the rules
		for rule in Inflector._plural['rulesOrderedKeys']:
			replacement = Inflector._plural['rules'][rule]
			testMatches = re.findall(rule, word, re.IGNORECASE)
			if len(testMatches) > 0:
				Inflector._cache('pluralize', word, re.sub(rule, replacement, word, re.IGNORECASE))
				return Inflector._cache('pluralize', word)
				
		return word
				
	"""
	/**
	 * @method singularize
	 * Returns word in singular form.
	 *
	 * @param string word The word in plural form
	 *
	 * @return string
	 * @author Patrick K
	 */
	"""
	@staticmethod
	def singularize(word):
		# just to be sure
		word = str(word)
		
		# get cache and check the return
		singularCache = Inflector._cache('singularize', word)
		if singularCache is not None:
			return singularCache
			
		# check for merged
		if 'merged' not in Inflector._singular:
			Inflector._singular['merged'] = {}
		# check for merged irregular
		if 'irregular' not in Inflector._singular['merged']:
			z = Inflector._singular['irregular'].copy()
			z.update({v:k for k, v in Inflector._plural['irregular'].iteritems()})
			Inflector._singular['merged']['irregular'] = z
		# check for merged uninflectored
		if 'uninflected' not in Inflector._singular['merged']:
			Inflector._singular['merged']['uninflected'] = Inflector._singular['uninflected'] + Inflector._uninflected
			
		# check for singular caches
		if 'cacheUninflected' not in Inflector._singular or 'cacheIrregular' not in Inflector._singular:
			Inflector._singular['cacheUninflected'] = '(?:' + '|'.join(Inflector._singular['merged']['uninflected']) + ')'
			Inflector._singular['cacheIrregular'] = '(?:' + '|'.join(Inflector._singular['merged']['irregular'].keys()) + ')'
		
		# search for irregular string
		irregularMatches = re.findall('(.*)\\b(' + Inflector._singular['cacheIrregular'] + ')$', word, re.IGNORECASE)
		if len(irregularMatches) > 0:
			Inflector._cache('singularize', word, Inflector._singular['merged']['irregular'][irregularMatches[-1][-1]])
			return Inflector._cache('singularize', word)
			
		# search for uninflectable string
		uninflectedMatches = re.findall('^(' + Inflector._singular['cacheUninflected'] + ')$', word, re.IGNORECASE)
		if len(uninflectedMatches) > 0:
			Inflector._cache('singularize', word, word)
			return Inflector._cache('singularize', word)
			
		# run through the rules
		for rule in Inflector._singular['rulesOrderedKeys']:
			replacement = Inflector._singular['rules'][rule]
			testMatches = re.findall(rule, word, re.IGNORECASE)
			if len(testMatches) > 0:
				Inflector._cache('singularize', word, re.sub(rule, replacement, word, re.IGNORECASE))
				return Inflector._cache('singularize', word)
				
		return word
	
	"""
	/**
	 * @method camelize
	 * Returns a lowercased and underscored string in camel case.
	 *
	 * @param string lowerCaseAndUnderscoredWord The word in underscored and lowercase form
	 *
	 * @return string
	 * @author Patrick K
	 */
	"""			
	@staticmethod
	def camelize(lowerCaseAndUnderscoredWord):
		# just to be sure
		lowerCaseAndUnderscoredWord = str(lowerCaseAndUnderscoredWord)
		
		# get cache and check the return
		camelizeCache = Inflector._cache('camelize', lowerCaseAndUnderscoredWord)
		if camelizeCache is not None:
			return camelizeCache
			
		Inflector._cache('camelize', lowerCaseAndUnderscoredWord, Inflector.humanize(lowerCaseAndUnderscoredWord).replace(' ', ''))
		return Inflector._cache('camelize', lowerCaseAndUnderscoredWord)
	
	"""
	/**
	 * @method underscore
	 * Returns a camel cased string in underscore form.
	 *
	 * @param string camelCasedWord The word in camelCased form
	 *
	 * @return string
	 * @author Patrick K
	 */
	"""		
	@staticmethod
	def underscore(camelCasedWord):
		# just to be sure
		camelCasedWord = str(camelCasedWord)
		
		# get cache and check the return
		underscoreCache = Inflector._cache('underscore', camelCasedWord)
		if underscoreCache is not None:
			return underscoreCache
		
		# do the conversion	
		s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camelCasedWord)
		s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
			
		Inflector._cache('underscore', camelCasedWord, s2)
		return Inflector._cache('underscore', camelCasedWord)
	
	"""
	/**
	 * @method humanize
	 * Returns the given underscored_word_group as a Human Readable Word Group.
	 * (Underscores are replaced by spaces and capitalized following words.)
	 *
	 * @param string lowerCaseAndUnderscoredWord String to be made more readable
	 *
	 * @return string
	 * @author Patrick K
	 */
	"""	
	@staticmethod
	def humanize(lowerCaseAndUnderscoredWord):
		# just to be sure
		lowerCaseAndUnderscoredWord = str(lowerCaseAndUnderscoredWord)
		
		# get cache and check the return
		humanizeCache = Inflector._cache('humanize', lowerCaseAndUnderscoredWord)
		if humanizeCache is not None:
			return humanizeCache
			
		Inflector._cache('humanize', lowerCaseAndUnderscoredWord, lowerCaseAndUnderscoredWord.replace('_', ' ').title())
		return Inflector._cache('humanize', lowerCaseAndUnderscoredWord)
	
	"""
	/**
	 * @method humanize
	 * Returns corresponding table name for given model $className. ("people" for the model class "Person").
	 *
	 * @param string className Name of class to get database table name for
	 *
	 * @return string
	 * @author Patrick K
	 */
	"""		
	@staticmethod
	def tableize(className):
		# just to be sure
		className = str(className)
		
		# get cache and check the return
		tableizeCache = Inflector._cache('tableize', className)
		if tableizeCache is not None:
			return tableizeCache
			
		Inflector._cache('tableize', className, Inflector.pluralize(Inflector.underscore(className)));
		return Inflector._cache('tableize', className)
		
	"""
	/**
	 * @method classify
	 * Returns Cake model class name ("Person" for the database table "people".) for given database table.
	 *
	 * @param string tableName Name of database table to get class name for
	 *
	 * @return string
	 * @author Patrick K
	 */
	"""
	@staticmethod
	def classify(tableName):
		# just to be sure
		tableName = str(tableName)
		
		# get cache and check the return
		classifyCache = Inflector._cache('classify', tableName)
		if classifyCache is not None:
			return classifyCache
									
		Inflector._cache('classify', tableName, Inflector.camelize(Inflector.singularize(Inflector.humanize(tableName))));
		return Inflector._cache('classify', tableName)
		
	"""
	/**
	 * @method variable
	 * Returns camelBacked version of an underscored string.
	 *
	 * @param string string String to convert.
	 *
	 * @return string
	 * @author Patrick K
	 */
	"""
	@staticmethod
	def variable(string):
		# just to be sure
		string = str(string)
		
		# get cache and check the return
		variableCache = Inflector._cache('variable', string)
		if variableCache is not None:
			return variableCache
			
		# camelize properly
		camelized = Inflector.camelize(Inflector.underscore(string))
		camelizedLst = list(camelized)
		camelizedLst[0] = camelizedLst[0].lower()
		camelized = "".join(camelizedLst)
		
		Inflector._cache('variable', string, camelized);
		return Inflector._cache('variable', string)
	
	"""
	/**
	 * @method slug
	 * Returns a string with all spaces converted to underscores (by default), accented
	 * characters converted to non-accented characters, and non word characters removed.
	 *
	 * @param string string the string you want to slug
	 * @param string replacement will replace keys in map
	 *
	 * @return string
	 * @author Patrick K
	 */
	"""	
	@staticmethod
	def slug(string, replacement = '-'):
		# just to be sure
		string = str(string)
		
		# get cache and check the return
		slugCache = Inflector._cache('slug', string)
		if slugCache is not None:
			return slugCache
			
		# the escaped replacement
		escReplacement = re.escape(replacement)
		
		# map changes needed to alter string with replacement
		aftString = re.sub('[^a-zA-Z0-9%s]' % escReplacement, replacement, string)
		aftString = aftString.replace('%s%s' % (replacement, replacement), replacement).lower()
		aftString = aftString.replace(replacement, ' ').strip()
		aftString = ' '.join(aftString.split()).replace(' ', replacement)
			
		# add to cache - random
		Inflector._cache('slug', string, aftString)
		return Inflector._cache('slug', string)
