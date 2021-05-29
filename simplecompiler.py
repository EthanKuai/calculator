import re


class SimpleCompiler:
	def __init__(self):
		self.REPLACECHARS = {
			' ':'', '{':'(', '}':')', '[':'(', ']':')', '+-':'-', '-+':'-',
			'\\pi':'3.14159265359', 'e': '2.718281828459'
		}
		self.LEGALCHARS = '.0123456789+-*/^()[]\{\}!; e pi'

	# input a string with statements separated by ';' for multiple results
	def inn(self, ss: str):
		ss = ss.split(';')
		results = []
		for s in ss:
			arr = self.__parse(s)
			if type(arr) == str: # Input Error
				results += arr
			else:
				results += str(self.__process(arr))
		return results

	# reads arr & recursively returns computed product
	def __process(self, arr: list):
		pass

	# sanitise & splits string into array
	def __parse(self, s: str):
		# standarise string for easier parsing
		for i in self.REPLACECHARS.keys():
			s = s.replace(i, self.REPLACECHARS[i])

		# check for illegal characters
		for char in s:
			if not char in self.LEGALCHARS:
				return f'Error! Illegal character "{char}". List of accepted characters: {self.LEGALCHARS}'

		# check	 boundary conditions
		if re.match(r"[0-9]", s):
			return f'Error! Mathematical expressions must start and end with numbers or brackets!'

		# convert s to an array
		arr = [s[0]]
		for char in s[1:]:
			pass

		# check no 2 operations are side-by-side


		# check for illegal bracket placements

		return arr
