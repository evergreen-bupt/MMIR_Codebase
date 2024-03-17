torchrun --standalone --nnodes 1 --nproc-per-node 2 scripts/pretrain.py \
  --model.type "one-stage+7b" \
  --model.model_id "kangz_prismatic_test" \
  --model.vision_backbone_id "clip-vit-l" \
  --model.image_resize_strategy "letterbox" \
  --model.llm_backbone_id "llama2-7b-pure"