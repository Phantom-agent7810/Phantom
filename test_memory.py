from memory.manager import MemoryManager

memory = MemoryManager()

memory.remember("weight", "97 kg")
print("Remember:", memory.recall("weight"))

memory.update("weight", "95 kg")
print("Updated:", memory.recall("weight"))

memory.forget("weight")
print("Forgot:", memory.recall("weight"))
