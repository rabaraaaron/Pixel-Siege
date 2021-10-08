from Models.SpriteSheetConverter import SpriteSheetConverter


class Character:

  def __init__(self, cName, fName):
    self.characterName = cName
    self.fileName = fName
    self.converter = SpriteSheetConverter(fName)
    self.holdFrame = self.converter.getHoldFrame()
    list = self.converter.getFrameNames()
    self.animationList = []
    self.attacking = False
    self.releasing = False
    self.index = 0
    self.color = self.converter.getAttackColor()
    for x in list:
      self.animationList.append(self.converter.parseSprite(x))

  def getName(self):
    return self.characterName

  def getFileName(self):
    return self.characterName

  def setAnimationFileName(self, fName):
    self.fileName = fName
    self.index = 0
    self.converter = SpriteSheetConverter(fName)
    list = self.converter.getFrameNames()
    self.holdFrame = self.converter.getHoldFrame()
    self.animationList = []
    for x in list:
      self.animationList.append(self.converter.parseSprite(x))


  def getHoldFrame(self):
    return self.holdFrame

  

