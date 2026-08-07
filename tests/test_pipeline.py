from src.pipeline.pipeline_manager import PipelineManager

pipeline = PipelineManager()

result = pipeline.run()

print("\n========== FINAL DATASET ==========\n")

print(result.head())

print("\nFinal Shape:")

print(result.shape)