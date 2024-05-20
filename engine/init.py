from transformers import AutoProcessor, BlipForQuestionAnswering, ViltProcessor, ViltForQuestionAnswering, CLIPModel, CLIPProcessor

## a initiate code for downloading and installing the required pretraining models, including:

# AutoProcessor.from_pretrained("Salesforce/blip-vqa-capfilt-large")
# BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-capfilt-large").to(self.device)
# ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
# ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa").to(self.device)
# CLIPModel.from_pretrained("openai/clip-vit-large-patch14")
# CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")
# ViltProcessor.from_pretrained("openai/vil-large-coco")
# ViltForQuestionAnswering.from_pretrained("openai/vil-large-coco")
# ViltProcessor.from_pretrained("openai/clip-vit-base-patch32")
# ViltForQuestionAnswering.from_pretrained("openai/clip-vit-base-patch32")


# Download and install the required pretraining models

# Path: engine/init.py
from transformers import AutoProcessor, BlipForQuestionAnswering, ViltProcessor, ViltForQuestionAnswering, CLIPModel, CLIPProcessor

model1 = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-capfilt-large")
model2 = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model3 = CLIPModel.from_pretrained("openai/clip-vit-large-patch14")
# model4 = ViltForQuestionAnswering.from_pretrained("openai/vil-large-coco")
model5 = ViltForQuestionAnswering.from_pretrained("openai/clip-vit-base-patch32")
print("Models are downloaded and installed successfully")