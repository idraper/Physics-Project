import numpy as np
from scipy.io import wavfile

from key import Key

class Wav_Manager():
	def __init__(self, fs=128000, s=128000, a=100, t=10):
		self.A = a
		self.Fs = fs
		self.sample = s
		self.frequencies = None
		self.x = np.arange(self.sample*t)
		self.sum = np.zeros(self.sample*t)
		self.y = None

	def newWave(self, freq):
		self.frequencies = freq
		self.sumWaves(freq)
		
	def sumWaves(self, freq):
		for f in freq:
			self.sum = self.sum + np.sin(2 * np.pi * f * self.x/self.Fs)
		self.y = np.array(self.A * self.sum, dtype='int16')
		print (self.y)
		
	def saveToFile(self, file='test.wav'):
		wavfile.write(file, self.Fs, self.y)
		
if __name__ == "__main__":
	'''
	k = Key("\nParagraphs \n\
	What this handout is about \n\
	This handout will help you understand how paragraphs are formed, how to develop stronger paragraphs, and how to completely and clearly express your ideas. \n\
	\n\
	What is a paragraph?\n\
	Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main idea. In this handout, we will refer to this as the “controlling idea,” because it controls what happens in the rest of the paragraph.\n\
	\n\
	How do I decide what to put in a paragraph?\n\
	Before you can begin to determine what the composition of a particular paragraph will be, you must first decide on an argument and a working thesis statement for your paper. What is the most important idea that you are trying to convey to your reader? The information in each paragraph must be related to that idea. In other words, your paragraphs should remind your reader that there is a recurrent relationship between your thesis and the information in each paragraph. A working thesis functions like a seed from which your paper, and your ideas, will grow. The whole process is an organic one—a natural progression from a seed to a full-blown paper where there are direct, familial relationships between all of the ideas in the paper.\n\
	\n\
	The decision about what to put into your paragraphs begins with the germination of a seed of ideas; this “germination process” is better known as brainstorming. There are many techniques for brainstorming; whichever one you choose, this stage of paragraph development cannot be skipped. Building paragraphs can be like building a skyscraper: there must be a well-planned foundation that supports what you are building. Any cracks, inconsistencies, or other corruptions of the foundation can cause your whole paper to crumble.\n\
	\n\
	So, let’s suppose that you have done some brainstorming to develop your thesis. What else should you keep in mind as you begin to create paragraphs? Every paragraph in a paper should be:\n\
	\n\
	Unified: All of the sentences in a single paragraph should be related to a single controlling idea (often expressed in the topic sentence of the paragraph).\n\
	Clearly related to the thesis: The sentences should all refer to the central idea, or thesis, of the paper (Rosen and Behrens 119).\n\
	Coherent: The sentences should be arranged in a logical manner and should follow a definite plan for development (Rosen and Behrens 119).\n\
	Well-developed: Every idea discussed in the paragraph should be adequately explained and supported through evidence and details that work together to explain the paragraph’s controlling idea (Rosen and Behrens 119).\n\
	How do I organize a paragraph?\n\
	There are many different ways to organize a paragraph. The organization you choose will depend on the controlling idea of the paragraph. Below are a few possibilities for organization, with links to brief examples:\n\
	\n\
	Narration: Tell a story. Go chronologically, from start to finish. (See an example.)\n\
	Description: Provide specific details about what something looks, smells, tastes, sounds, or feels like. Organize spatially, in order of appearance, or by topic. (See an example.)\n\
	Process: Explain how something works, step by step. Perhaps follow a sequence—first, second, third. (See an example.)\n\
	Classification: Separate into groups or explain the various parts of a topic. (See an example.)\n\
	Illustration: Give examples and explain how those examples prove your point. (See the detailed example in the next section of this handout.)\n\
	5-step process to paragraph development\n\
	Let’s walk through a 5-step process for building a paragraph. For each step there is an explanation and example. Our example paragraph will be about slave spirituals, the original songs that African Americans created during slavery. The model paragraph uses illustration (giving examples) to prove its point.\n\
	\n\
	Step 1. Decide on a controlling idea and create a topic sentence\n\
	Paragraph development begins with the formulation of the controlling idea. This idea directs the paragraph’s development. Often, the controlling idea of a paragraph will appear in the form of a topic sentence. In some cases, you may need more than one sentence to express a paragraph’s controlling idea. Here is the controlling idea for our “model paragraph,” expressed in a topic sentence:\n\
	\n\
	Model controlling idea and topic sentence — Slave spirituals often had hidden double meanings.\n\
	Step 2. Explain the controlling idea\n\
	Paragraph development continues with an expression of the rationale or the explanation that the writer gives for how the reader should interpret the information presented in the idea statement or topic sentence of the paragraph. The writer explains his/her thinking about the main topic, idea, or focus of the paragraph. Here’s the sentence that would follow the controlling idea about slave spirituals:\n\
	\n\
	Model explanation — On one level, spirituals referenced heaven, Jesus, and the soul; but on another level, the songs spoke about slave resistance.\n\
	Step 3. Give an example (or multiple examples)\n\
	Paragraph development progresses with the expression of some type of support or evidence for the idea and the explanation that came before it. The example serves as a sign or representation of the relationship established in the idea and explanation portions of the paragraph. Here are two examples that we could use to illustrate the double meanings in slave spirituals:\n\
	\n\
	Model example A — For example, according to Frederick Douglass, the song “O Canaan, Sweet Canaan” spoke of slaves’ longing for heaven, but it also expressed their desire to escape to the North. Careful listeners heard this second meaning in the following lyrics: “I don’t expect to stay / Much longer here. / Run to Jesus, shun the danger. / I don’t expect to stay.”\n\
	Model example B — Slaves even used songs like “Steal Away to Jesus (at midnight)” to announce to other slaves the time and place of secret, forbidden meetings.\n\
	Step 4. Explain the example(s)\n\
	The next movement in paragraph development is an explanation of each example and its relevance to the topic sentence and rationale that were stated at the beginning of the paragraph. This explanation shows readers why you chose to use this/or these particular examples as evidence to support the major claim, or focus, in your paragraph.\n\
	\n\
	Continue the pattern of giving examples and explaining them until all points/examples that the writer deems necessary have been made and explained. NONE of your examples should be left unexplained. You might be able to explain the relationship between the example and the topic sentence in the same sentence which introduced the example. More often, however, you will need to explain that relationship in a separate sentence. Look at these explanations for the two examples in the slave spirituals paragraph:\n\
	\n\
	Model explanation for example A — When slaves sang this song, they could have been speaking of their departure from this life and their arrival in heaven; however, they also could have been describing their plans to leave the South and run, not to Jesus, but to the North.\n\
	Model explanation for example B — [The relationship between example B and the main idea of the paragraph’s controlling idea is clear enough without adding another sentence to explain it.]\n\
	Step 5. Complete the paragraph’s idea or transition into the next paragraph\n\
	The final movement in paragraph development involves tying up the loose ends of the paragraph and reminding the reader of the relevance of the information in this paragraph to the main or controlling idea of the paper. At this point, you can remind your reader about the relevance of the information that you just discussed in the paragraph. You might feel more comfortable, however, simply transitioning your reader to the next development in the next paragraph. Here’s an example of a sentence that completes the slave spirituals paragraph:\n\
	\n\
	Model sentence for completing a paragraph — What whites heard as merely spiritual songs, slaves discerned as detailed messages. The hidden meanings in spirituals allowed slaves to sing what they could not say.\n\
	Notice that the example and explanation steps of this 5-step process (steps 3 and 4) can be repeated as needed. The idea is that you continue to use this pattern until you have completely developed the main idea of the paragraph.\n\
	\n\
	Here is a look at the completed “model” paragraph:\n\
	Slave spirituals often had hidden double meanings. On one level, spirituals referenced heaven, Jesus, and the soul, but on another level, the songs spoke about slave resistance. For example, according to Frederick Douglass, the song “O Canaan, Sweet Canaan” spoke of slaves’ longing for heaven, but it also expressed their desire to escape to the North. Careful listeners heard this second meaning in the following lyrics: “I don’t expect to stay / Much longer here. / Run to Jesus, shun the danger. / I don’t expect to stay.” When slaves sang this song, they could have been speaking of their departure from this life and their arrival in heaven; however, they also could have been describing their plans to leave the South and run, not to Jesus, but to the North. Slaves even used songs like “Steal Away to Jesus (at midnight)” to announce to other slaves the time and place of secret, forbidden meetings. What whites heard as merely spiritual songs, slaves discerned as detailed messages. The hidden meanings in spirituals allowed slaves to sing what they could not say.')\n\
	")
	'''
	
	#k = Key("abcdefghijklmnopqrstuvwxyz.)'/\\,ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890(*&^%")
	k = Key(" !\"#$%'()*+,-./1234567890:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]\\^_`~abc")
	print ('Original:\n', k.getMessage())
	k.saveToFile()
	print ()
	print ('Decoded from file:\n', k.decodeMessage(k.getMessageLexo()))
	print ()
	print (k.getFrequencies())
	
	w = Wav_Manager()
	w.newWave(k.getFrequencies())
	w.saveToFile()
	
	
	
