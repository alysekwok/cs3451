// Fragment shader

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_LIGHT_SHADER

uniform float cx;
uniform float cy;

// These values come from the vertex shader
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying vec4 vertTexCoord;

void main() { 
  vec2 z = vec2(vertTexCoord.x * 6.38 - 3.14, vertTexCoord.y * 6.38 - 3.14);
  for (int i = 0; i < 20; i++) {
    vec2 sine = vec2(sin(z.x)*cosh(z.y), cos(z.x)*sinh(z.y));
    z = vec2(cx * sine.x - cy * sine.y, cx * sine.y + cy * sine.x);

  }
  vec4 diffuse_color = vec4(1.0, 0.0, 0.0, 1.0);
  if (length(z) < (50 * 50)) {
     diffuse_color = vec4(1.0, 1.0, 1.0, 1.0);
  }
  float diffuse = clamp(dot(vertNormal, vertLightDir),0.0,1.0);
  gl_FragColor = vec4(diffuse * diffuse_color.rgb, 1.0);

}