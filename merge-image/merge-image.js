const Jimp = require("jimp");

async function mergeMultipleImages(imagePaths, outputPath) {
  // 加载所有图片
  const images = await Promise.all(imagePaths.map((path) => Jimp.read(path)));

  // 计算总宽度和总高度
  const totalWidth = Math.max(...images.map((img) => img.getWidth()));
  const totalHeight = images.reduce((sum, img) => sum + img.getHeight(), 0);

  // 创建新图片
  const mergedImage = new Jimp(totalWidth, totalHeight);

  // 合并图片
  let y = 0;
  for (let img of images) {
    mergedImage.composite(img, 0, y);
    y += img.getHeight();
  }

  // 保存
  mergedImage.write(outputPath);
}

// 示例使用
const imagePaths = [
  "../../纳税证明1.jpg",
  "../../纳税证明2.jpg",
  "../../纳税明细.jpg",
  "../../2022年终汇算整合.jpg",
]; // 可以添加更多图片路径
mergeMultipleImages(imagePaths, "merged_image.jpg");
