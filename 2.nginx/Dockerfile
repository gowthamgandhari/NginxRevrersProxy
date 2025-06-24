FROM nginx:alpine

# Remove the default config (from conf.d)
RUN rm /etc/nginx/conf.d/default.conf

# Copy your edited config from /sites-available/default
COPY default /etc/nginx/conf.d/default.conf

EXPOSE 8080
